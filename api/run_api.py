import uvicorn
import api_app

if __name__ == "__main__":
    uvicorn.run("api_app.api:app", host="127.0.0.1", port=5000, log_level="info")