#!/usr/bin/env python3
"""grok-relay: call GitHub Models (xai/grok-3) for each unprocessed request.

Reads every file in grok-relay/requests/, sends its whole content as the
user prompt, and writes the answer text to grok-relay/responses/<same name>.
Requests that already have a response file (or an error file) are skipped.

On API failure, writes grok-relay/responses/<name>.error.md with the HTTP
status and response body so the failure is visible in the repo. The API
token is read from the GITHUB_TOKEN environment variable only; it is never
written to a file or printed.
"""

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REQUESTS = ROOT / "requests"
RESPONSES = ROOT / "responses"
ENDPOINT = "https://models.github.ai/inference/chat/completions"
MODEL = "xai/grok-3"


def call_model(prompt: str, token: str) -> str:
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
    }
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        print("GITHUB_TOKEN is not set", file=sys.stderr)
        return 1
    RESPONSES.mkdir(exist_ok=True)
    failures = 0
    for req_path in sorted(REQUESTS.glob("*")):
        if not req_path.is_file():
            continue
        name = req_path.name
        out_path = RESPONSES / name
        err_path = RESPONSES / (name + ".error.md")
        if out_path.exists() or err_path.exists():
            print(f"skip {name}: already processed")
            continue
        prompt = req_path.read_text(encoding="utf-8")
        print(f"processing {name} ({len(prompt)} chars)")
        try:
            answer = call_model(prompt, token)
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            err_path.write_text(
                f"# Error for {name}\n\nHTTP {e.code} {e.reason}\n\n```\n{body}\n```\n",
                encoding="utf-8",
            )
            print(f"error {name}: HTTP {e.code}")
            failures += 1
            continue
        except Exception as e:
            err_path.write_text(
                f"# Error for {name}\n\n{type(e).__name__}: {e}\n",
                encoding="utf-8",
            )
            print(f"error {name}: {e}")
            failures += 1
            continue
        out_path.write_text(answer.rstrip() + "\n", encoding="utf-8")
        print(f"done {name}: {len(answer)} chars")
    print(f"finished, failures={failures}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
