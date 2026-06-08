from fastapi import FastAPI

app = FastAPI()


@app.get("/all")
async def products():
    return {
        "service":
            "products"
    }
