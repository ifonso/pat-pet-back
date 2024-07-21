import uvicorn


if __name__ == "__main__":
    uvicorn.run("src.app:app", port=80, log_level="warning", host="0.0.0.0")
