from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import analyze, roadmap, chat

app = FastAPI(
    title="AI Career Gap Analyzer API",
    description="API for analyzing resumes, finding skill gaps, and generating learning roadmaps.",
    version="1.0.0"
)

# Configure CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the exact frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(analyze.router, prefix="/api", tags=["analyze"])
app.include_router(roadmap.router, prefix="/api", tags=["roadmap"])
app.include_router(chat.router, prefix="/api", tags=["chat"])

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Career Gap Analyzer API. Visit /docs for API documentation."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
