import os

print("🤖 AI Code Review Started\n")

def review_code(file_path, code):
    issues = []

    for line_no, line in enumerate(code.splitlines(), start=1):
        stripped = line.strip()

        # Rule 1: function definition missing colon
        if stripped.startswith("def ") and not stripped.endswith(":"):
            issues.append(
                f"❌ Line {line_no}: Function definition missing ':'\n"
                f"   ✅ Suggested fix: {stripped}:"
            )

        # Rule 2: print used for debugging
        if "print(" in stripped:
            issues.append(
                f"⚠️ Line {line_no}: Debug print statement found\n"
                f"   💡 Consider using logging or removing it"
            )

        # Rule 3: very short variable names
        if "=" in stripped:
            left = stripped.split("=")[0].strip()
            if len(left) == 1:
                issues.append(
                    f"⚠️ Line {line_no}: Variable name '{left}' is too short\n"
                    f"   💡 Use more descriptive variable names"
                )

    if not issues:
        print("✅ No obvious issues found\n")
    else:
        for issue in issues:
            print(issue)
        print()

for root, dirs, files in os.walk("."):
    if "venv" in root or ".git" in root or "scripts" in root:
        continue

    for file in files:
        if file.endswith(".py"):
            path = os.path.join(root, file)
            print(f"📄 Reviewing: {path}")

            with open(path, "r", encoding="utf-8") as f:
                code = f.read()

            review_code(path, code)
