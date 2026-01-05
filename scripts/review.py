import os

print("🤖 AI Code Review Started\n")

def review_code(file_path, code):
    issues = []

    # Rule 1: function definition missing colon
    for line_no, line in enumerate(code.splitlines(), start=1):
        if line.strip().startswith("def ") and not line.strip().endswith(":"):
            issues.append(
                f"❌ Line {line_no}: Function definition missing ':'\n"
                f"   ✅ Suggested fix: {line.strip()}:"
            )

    if not issues:
        print("✅ No obvious issues found\n")
    else:
        for issue in issues:
            print(issue)
        print()

for root, dirs, files in os.walk("."):
    if "venv" in root or ".git" in root:
        continue

    for file in files:
        if file.endswith(".py"):
            path = os.path.join(root, file)
            print(f"📄 Reviewing: {path}")

            with open(path, "r", encoding="utf-8") as f:
                code = f.read()

            review_code(path, code)
