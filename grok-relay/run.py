#!/usr/bin/env python3
"""grok-relay: call GitHub Models (xai/grok-3) for each unprocessed request.

Reads every file in grok-relay/requests/, sends its whole content as the
user prompt, and writes the answer text to grok-relay/responses/<same name>.
Requests that already have a response file (or an error file) are skipped.

On API failure, writes grok-relay/responses/<name>.error.md with the HTTP
status, the Content-Type and the first 1000 characters of the raw response
body (captured before any JSON parsing) so the failure is visible in the
repo. The API token is read from the GITHUB_TOKEN environment variable
only; it is never written to a file or printed.
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


class ApiResponseError(Exception):
    """An HTTP response was received but could not be used.

    Carries the raw response details (status, Content-Type, body) captured
    before JSON parsing, so they can be recorded in the error file.
    """

    def __init__(self, status, content_type, body, note):
        super().__init__(note)
        self.status = status
        self.content_type = content_type
        self.body = body
        self.note = note


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
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            status = resp.status
            content_type = resp.headers.get("Content-Type", "")
            raw = resp.read()
    except urllib.error.HTTPError as e:
        raw = e.read()
        raise ApiResponseError(
            e.code,
            e.headers.get("Content-Type", "") if e.headers else "",
            raw.decode("utf-8", errors="replace"),
            f"HTTP {e.code} {e.reason}",
        ) from e
    body = raw.decode("utf-8", errors="replace")
    if status != 200:
        raise ApiResponseError(status, content_type, body, f"HTTP {status}")
    try:
        data = json.loads(body)
    except json.JSONDecodeError as e:
        raise ApiResponseError(
            status, content_type, body, f"JSONDecodeError: {e}"
        ) from e
    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as e:
        raise ApiResponseError(
            status, content_type, body, f"Unexpected JSON structure: {e}"
        ) from e


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
        except ApiResponseError as e:
            err_path.write_text(
                f"# Error for {name}\n\n"
                f"- HTTP status: {e.status}\n"
                f"- Content-Type: {e.content_type}\n"
                f"- Detail: {e.note}\n\n"
                f"Response body (first 1000 chars):\n\n```\n{e.body[:1000]}\n```\n",
                encoding="utf-8",
            )
            print(f"error {name}: HTTP {e.status} ({e.note})")
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
