import os

print("🤖 AI Code Review Started")

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py") and "venv" not in root:
            print("\n📄 Reviewing:", os.path.join(root, file))
            with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                code = f.read()
                print(code[:500])  # print first 500 chars
