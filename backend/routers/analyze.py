from fastapi import APIRouter, File, UploadFile, Form, HTTPException
from models.api_models import GapAnalysisResponse
from services.nlp_service import extract_text_from_file, extract_skills
from services.db_service import save_gap_analysis

router = APIRouter()

@router.post("/analyze", response_model=GapAnalysisResponse)
async def analyze_resume(
    target_role: str = Form(...),
    file: UploadFile = File(...)
):
    try:
        # 1. Extract text from the uploaded file
        text = await extract_text_from_file(file)
        
        # 2. Extract skills and calculate gap
        existing_skills, missing_skills, match_percentage = extract_skills(text, target_role)
        
        # 3. Prepare response data
        analysis_data = {
            "target_role": target_role,
            "existing_skills": existing_skills,
            "missing_skills": missing_skills,
            "match_percentage": match_percentage
        }
        
        # 4. Save to database
        db_id = await save_gap_analysis(analysis_data)
        analysis_data["id"] = db_id
        
        return GapAnalysisResponse(**analysis_data)
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Error in analyze_resume: {e}")
        raise HTTPException(status_code=500, detail="An error occurred during analysis.")
