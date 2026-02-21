import nltk
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from app.routes.analyze import router as analyze_router
from app.routes.roles import router as roles_router
from app.core.config import settings
from app.core.logger import logging_middleware, logger

def init_app() -> FastAPI:
    # Inicializa o FastAPI
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )

    # Middleware
    app.add_middleware(BaseHTTPMiddleware, dispatch=logging_middleware)

    # Inicialização do NLTK
    @app.on_event("startup")
    async def startup_event():
        logger.info("Baixando dados do NLTK...", extra={"severity": "INFO"})
        try:
            nltk.download('punkt')
            nltk.download('stopwords')
            nltk.download('punkt_tab') # Adicionado para melhor compatibilidade
        except Exception as e:
            logger.error(f"Falha no download do NLTK: {str(e)}", extra={"severity": "ERROR"})

    @app.get("/health")
    def health():
        return {"status": "ok", "app": settings.PROJECT_NAME, "version": settings.VERSION}

    # Rotas
    app.include_router(analyze_router, prefix=settings.API_V1_STR, tags=["Analysis"])
    app.include_router(roles_router, prefix=settings.API_V1_STR, tags=["Roles"])

    return app

app = init_app()
