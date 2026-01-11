import os
import requests
from pathlib import Path

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API = "https://api.github.com"

def post_pr_comment(message):
    repo = os.getenv("GITHUB_REPOSITORY")
    event_path = os.getenv("GITHUB_EVENT_PATH")

    if not repo or not event_path:
        print("Not running in PR context.")
        return

    with open(event_path) as f:
        event = __import__("json").load(f)

    pr_number = event["pull_request"]["number"]

    url = f"{GITHUB_API}/repos/{repo}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.post(url, headers=headers, json={"body": message})
    print("Comment posted:", response.status_code)


def mock_ai_review(code):
    issues = []

    if "print(" in code:
        issues.append("Avoid leaving debug print statements in production code.")

    if "def " in code and ":" not in code.split("\n")[0]:
        issues.append("Function definition might be missing a colon `:`.")

    if not issues:
        return "✅ No major issues found."

    return "\n".join(f"- {issue}" for issue in issues)


def main():
    comments = ["🧠 **AI Code Review (Mock Mode)**\n"]

    for file in Path(".").rglob("*.py"):
        if ".venv" in str(file) or ".github" in str(file):
            continue

        code = file.read_text()
        review = mock_ai_review(code)

        comments.append(f"📄 **{file}**\n{review}\n")

    final_comment = "\n".join(comments)
    print(final_comment)
    post_pr_comment(final_comment)


if __name__ == "__main__":
    main()
