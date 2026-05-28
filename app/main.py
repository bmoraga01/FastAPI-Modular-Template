from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

from app.modules.products.routers import router as product

# FastApi instance
app = FastAPI()

# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.CORS_ORIGINS_URL
    ],  # Urls que pueden consumir el api
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los encabezados
)

# Routes
app.include_router(product, prefix="/api", tags=["products"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test")
async def test():
    return {"message": "It's Work!!"}
