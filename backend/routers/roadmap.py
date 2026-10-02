from fastapi import APIRouter, HTTPException
from models.api_models import RoadmapRequest, RoadmapResponse
from services.ai_service import generate_roadmap
from services.db_service import save_roadmap, get_gap_analysis

router = APIRouter()

@router.post("/roadmap", response_model=RoadmapResponse)
async def create_roadmap(request: RoadmapRequest):
    try:
        # If a gap_analysis_id is provided, we could optionally fetch it to verify or add context
        # but for now we just use the missing_skills provided in the request
        
        if not request.missing_skills:
            raise HTTPException(status_code=400, detail="No missing skills provided to generate a roadmap.")
            
        steps = await generate_roadmap(request.target_role, request.missing_skills)
        
        roadmap_data = {
            "target_role": request.target_role,
            "steps": [step.dict() for step in steps]
        }
        
        db_id = await save_roadmap(roadmap_data)
        
        # Prepare response
        return RoadmapResponse(
            id=db_id,
            target_role=request.target_role,
            steps=steps
        )
        
    except Exception as e:
        print(f"Error in create_roadmap: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while generating the roadmap.")

@router.get("/roadmap/{roadmap_id}", response_model=RoadmapResponse)
async def retrieve_roadmap(roadmap_id: str):
    from backend.services.db_service import get_roadmap
    
    roadmap_data = await get_roadmap(roadmap_id)
    if not roadmap_data:
        raise HTTPException(status_code=404, detail="Roadmap not found.")
        
    return RoadmapResponse(**roadmap_data)
