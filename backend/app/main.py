from fastapi import FastAPI

app = FastAPI(title="AutoJobMate API")

@app.get("/")
def root():
    return {"status": "AutoJobMate backend is running"}
