from fastapi import APIRouter
from app.core.config import settings
from app.models.schemas import RoleListResponse

router = APIRouter()

@router.get("/roles", response_model=RoleListResponse)
async def list_roles():
    """Retorna uma lista de cargos que possuem palavras-chave pré-definidas para correspondência."""
    return RoleListResponse(roles=settings.SUPPORTED_ROLES)
