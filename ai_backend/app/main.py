from fastapi import FastAPI

app = FastAPI(title="AI Backend")

@app.get("/health")
def health_check():
    return {"status": "ok"}
