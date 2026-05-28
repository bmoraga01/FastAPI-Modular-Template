from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.common.exceptions import AppException
from app.common.schemas.responses import MessageResponse
from app.core.config import settings

from app.modules.products.routers import router as product

# FastApi instance
app = FastAPI()


# Excepcions
@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.message,
            "errors": exc.errors,
        },
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
):
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Validation Error",
            "errors": exc.errors(),
        },
    )


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


@app.get("/", response_model=MessageResponse)
async def root():
    return MessageResponse(message="Hello World!!!")


@app.get("/test", response_model=MessageResponse)
async def test():
    return MessageResponse(message="It's Work!!")
