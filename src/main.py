from fastapi import FastAPI

app = FastAPI()


@app.get("/api/data")
async def get_data():
    return {"message": "Hello from FastAPI"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
