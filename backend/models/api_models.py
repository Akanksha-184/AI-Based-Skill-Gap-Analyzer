from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class AnalyzeRequest(BaseModel):
    target_role: str

class GapAnalysisResponse(BaseModel):
    id: str = Field(default="")
    target_role: str
    existing_skills: List[str]
    missing_skills: List[str]
    match_percentage: float

class RoadmapRequest(BaseModel):
    target_role: str
    missing_skills: List[str]
    gap_analysis_id: Optional[str] = None

class RoadmapStep(BaseModel):
    title: str
    description: str
    resources: List[str]
    estimated_time: str

class RoadmapResponse(BaseModel):
    id: str = Field(default="")
    target_role: str
    steps: List[RoadmapStep]

class ChatMessage(BaseModel):
    role: str # 'user' or 'assistant'
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatMessage]
    context: Optional[Dict[str, Any]] = None

class ChatResponse(BaseModel):
    reply: str
