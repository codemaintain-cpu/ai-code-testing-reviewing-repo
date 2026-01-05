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
    return response.choices[0].message.content
