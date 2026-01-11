import os
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_EVENT_PATH = os.getenv("GITHUB_EVENT_PATH")

def post_pr_comment(body):
    if not GITHUB_EVENT_PATH:
        print("Not running in a PR context")
        return

    import json
    with open(GITHUB_EVENT_PATH, "r") as f:
        event = json.load(f)

    pr = event.get("pull_request")
    if not pr:
        print("No pull request found")
        return

    comments_url = pr["comments_url"]

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.post(
        comments_url,
        headers=headers,
        json={"body": body}
    )

    if response.status_code == 201:
        print("✅ Comment posted on PR")
    else:
        print("❌ Failed to post comment:", response.text)


def run_review():
    review_output = []
    review_output.append("🧠 **AI Code Review (Mock Mode)**\n")

    # Mock findings
    review_output.append("📄 **buggy_example.py**")
    review_output.append("- Missing colon `:` in function definition")
    review_output.append("- Avoid leaving debug `print()` statements\n")

    comment_body = "\n".join(review_output)
    print(comment_body)

    post_pr_comment(comment_body)


if __name__ == "__main__":
    run_review()
