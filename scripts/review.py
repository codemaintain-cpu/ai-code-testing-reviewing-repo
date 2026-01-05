from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ai_review(code):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert code reviewer."},
            {"role": "user", "content": f"Review this code and suggest improvements:\n\n{code}"}
        ],
        temperature=0.2,
    )
    print("\n🧠 AI REVIEW RESULT:\n")

    for item in response.output:
        if item["type"] == "message":
            for content in item["content"]:
                if content["type"] == "output_text":
                    print(content["text"])

    review_text = response.choices[0].message.content
    print("\n🧠 AI REVIEW RESULT:\n")
    print(review_text)
    print("\n" + "-"*60 + "\n")
    return review_text

