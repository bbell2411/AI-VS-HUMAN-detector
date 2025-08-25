from fastapi import FastAPI
from app.config import settings
from app.routers import health
from app.routers import predictions
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    debug=settings.DEBUG
)
origins = [
    "http://localhost:3000", 
    "http://localhost:5173",  
    "https://textguard.netlify.app",  
    "https://textguard.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix=settings.API_V1_STR, tags=["health"])
app.include_router(predictions.router, prefix=settings.API_V1_STR, tags=["predictions"])
app.include_router(predictions.router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": "ML Text Detector API", "status": "running"}

