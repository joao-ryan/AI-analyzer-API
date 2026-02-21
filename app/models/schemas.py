from pydantic import BaseModel, Field
from typing import List, Optional

class AnalyzeRequest(BaseModel):
    job_role: str = Field(..., description="O cargo alvo para o candidato")
    job_description: Optional[str] = Field(None, description="Descrição específica da vaga opcional para correspondência")

class FeedbackDetail(BaseModel):
    strengths: List[str]
    weaknesses: List[str]
    suggestions: List[str]

class AnalyzeResponse(BaseModel):
    score: float = Field(..., description="Pontuação de correspondência ATS de 0 a 100")
    match_level: str = Field(..., description="Classificação: Júnior, Pleno ou Combinação Forte")
    matched_keywords: List[str]
    missing_keywords: List[str]
    feedback: FeedbackDetail

class RoleListResponse(BaseModel):
    roles: List[str]
