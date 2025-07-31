from fastapi import FastAPI
from app.config import settings
from app.routers import health

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    debug=settings.DEBUG
)

app.include_router(health.router, prefix=settings.API_V1_STR, tags=["health"])

@app.get("/")
def read_root():
    return {"message": "ML Text Detector API", "status": "running"}