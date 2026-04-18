from fastapi import FastAPI
from backend.api.nutrition_routes import router as nutrition_router

app = FastAPI(
    title="Gymmer API",
    description="RESTful API for fetching and storing nutrition data.",
    version="0.1.0"
)

app.include_router(nutrition_router)


@app.get("/")
def root():
    return {"message": "Gymmer API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}