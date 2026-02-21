from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import Optional
from app.services.resume_parser import extract_text_from_pdf
from app.services.scorer import calculate_score, get_match_level
from app.services.feedback import generate_feedback
from app.models.schemas import AnalyzeResponse, FeedbackDetail
from app.core.logger import logger

router = APIRouter()

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_resume(
    file: Optional[UploadFile] = File(None),
    resume_text: Optional[str] = Form(None),
    job_role: str = Form(...),
    job_description: Optional[str] = Form(None)
):
    try:
        # 1. Extração
        if file:
            content = extract_text_from_pdf(file.file)
        elif resume_text:
            content = resume_text
        else:
            raise HTTPException(status_code=400, detail="Forneça um arquivo PDF ou o texto do currículo.")

        # 2. Pontuação
        score, matched, missing = calculate_score(content, job_role, job_description)
        match_level = get_match_level(score)

        # 3. Feedback
        strengths, weaknesses, suggestions = generate_feedback(score, missing, matched)

        return AnalyzeResponse(
            score=score,
            match_level=match_level,
            matched_keywords=matched,
            missing_keywords=missing,
            feedback=FeedbackDetail(
                strengths=strengths,
                weaknesses=weaknesses,
                suggestions=suggestions
            )
        )
    except Exception as e:
        logger.error(f"Falha na análise: {str(e)}", extra={"severity": "ERROR"})
        raise HTTPException(status_code=500, detail=str(e))
