from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import chat
from contextlib import asynccontextmanager
from src.llm.assistant import MeisterAI


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Loading MeisterAI...")

    app.state.assistant = MeisterAI()

    print("MeisterAI ready.")

    yield

    print("Shutting down MeisterAI...")
    

app = FastAPI(
    title="MeisterAI API",
    description="Intelligent RAG backend for German vehicle repair diagnostics",
    version="1.0.0",
    lifespan=lifespan
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict this in production (e.g., ["http://localhost:3000"])
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(chat.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the MeisterAI RAG API. Visit /docs for Swagger UI."}

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "MeisterAI",
        "version": "1.0.0"
    }
    
@app.get("/health/live")
async def live():
    return {"alive": True}
    
@app.get("/ready")
async def ready():

    loaded = hasattr(app.state, "assistant")

    return {
        "ready": loaded
    }