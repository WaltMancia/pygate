from fastapi import FastAPI

app = FastAPI()


@app.get("/profile")
async def profile():
    return {
        "service": "users",
        "message":
            "profile endpoint"
    }
