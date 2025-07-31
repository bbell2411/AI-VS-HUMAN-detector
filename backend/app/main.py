from fastapi import FastAPI
from app.config import settings
from app.routers import health

# Create FastAPI app (like express())
app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    debug=settings.DEBUG
)

# Include routers (like app.use('/api', router))
app.include_router(health.router, prefix=settings.API_V1_STR, tags=["health"])

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "ML Text Detector API", "status": "running"}