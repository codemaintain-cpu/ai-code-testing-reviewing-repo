from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend is working!"}

@app.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()
    print("📦 GitHub Event Received")
    print(payload.keys())

    return {"status": "received"}
