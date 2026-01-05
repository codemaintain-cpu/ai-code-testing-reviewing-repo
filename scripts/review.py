import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

print("🤖 AI Code Review Started\n")

def ai_review(code):
    prompt = f"""
You are a senior software engineer.
Review the following code.
Point out bugs, bad practices, and suggest fixes clearly.

Code:
{code}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    return response.choices[0].message.content


for root, dirs, files in os.walk("."):
    if "venv" in root or ".git" in root or "scripts" in root:
        continue

    for file in files:
        if file.endswith(".py"):
            path = os.path.join(root, file)
            print(f"📄 Reviewing: {path}")

            with open(path, "r", encoding="utf-8") as f:
                code = f.read()

            review = ai_review(code)
            print(review)
            print("-" * 50)
