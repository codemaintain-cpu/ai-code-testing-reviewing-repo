import os

def ai_review(code: str) -> str:
    feedback = []

    # Basic checks
    if "print(" in code:
        feedback.append("• Avoid leaving debug print statements in production code.")

    if "def " in code and ":" not in code.split("def")[1]:
        feedback.append("• Function definition might be missing a colon `:`.")

    if "return" not in code:
        feedback.append("• Function does not return anything. Consider returning a value.")

    if not feedback:
        feedback.append("• Code looks clean. No obvious issues found.")

    return "\n".join(feedback)


def main():
    print("\n🧠 AI CODE REVIEW (Mock Mode)\n" + "-" * 40)

    for root, dirs, files in os.walk("."):
        if ".git" in root or "venv" in root:
            continue

        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)

                print(f"\n📄 Reviewing: {path}\n")

                with open(path, "r", encoding="utf-8") as f:
                    code = f.read()

                review = ai_review(code)
                print(review)
                print("\n" + "-" * 40)


if __name__ == "__main__":
    main()
