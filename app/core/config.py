import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Resume Analyzer API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api"

    # Cargos Suportados
    SUPPORTED_ROLES: list = [
        "Software Engineer",
        "Backend Developer",
        "Frontend Developer",
        "Fullstack Developer",
        "Data Scientist",
        "DevOps Engineer",
        "Product Manager",
        "Mobile Developer",
        "QA Engineer"
    ]

    # Configurações de NLP
    NLTK_DATA_PATH: str = "/tmp/nltk_data"

    class Config:
        case_sensitive = True

settings = Settings()
