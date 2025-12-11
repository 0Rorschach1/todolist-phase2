import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv


load_dotenv()


from app.api.v1.api_router import router as api_v1_router

app = FastAPI(
    title="ToDoList API - AUT 1403",
    description="""
    ## ToDoList RESTful API
    
    A clean, layered FastAPI application for managing projects and tasks.
    
    ### Features
    - Create, read, update, delete projects and tasks
    - Full Pydantic validation
    - Repository Pattern + Dependency Injection
    - PostgreSQL + SQLAlchemy + Alembic migrations
    - Auto-generated documentation
    
    ### Architecture (Layered)
    - `api/v1` → Presentation Layer (Routers)
    - `services` → Application/Business Logic
    - `repositories` → Data Access Layer
    - `models` + `schemas` → Domain Layer
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)
origins = os.getenv("CORS_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_v1_router, prefix="/api/v1")


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to ToDoList API",
        "version": "1.0.0",
        "documentation": "/docs",
        "health_check": "/health",
    }


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy", "service": "ToDoList API"}
