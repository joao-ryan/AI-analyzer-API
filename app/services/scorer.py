from app.services.nlp_service import nlp_service
from app.core.config import settings

ROLE_KEYWORDS = {
    "software engineer": "software development engineering programming git version control agile system design architecture",
    "backend developer": "python fastapi django flask nodejs java spring docker kubernetes postgresql sql api restful microservices redis aws",
    "frontend developer": "react angular vue javascript typescript html css sass tailwind nextjs webpack vite frontend web",
    "fullstack developer": "react nodejs python javascript typescript sql nosql api web development frontend backend",
    "data scientist": "python machine learning statistics pandas numpy scikit-learn tensorflow pytorch sql data analysis visualization",
    "devops engineer": "docker kubernetes terraform ansible cloud aws azure gcp ci/cd pipeline automation linux bash prometheus grafana",
    "product manager": "product management agile scrum roadmap backlog user stories stakeholder management strategy market research",
    "mobile developer": "react native flutter swift kotlin android ios mobile development app",
    "qa engineer": "testing automation selenium cypress jest unit testing integration testing bug tracking quality assurance"
}

def calculate_score(resume_text: str, job_role: str, specific_jd: str = None):
    # Usa a descrição da vaga (JD) específica se fornecida, caso contrário usa palavras-chave pré-definidas para o cargo
    target_text = specific_jd if specific_jd else ROLE_KEYWORDS.get(job_role.lower(), "")

    if not target_text and not specific_jd:
        # Fallback se o cargo não for encontrado e nenhuma descrição de vaga (JD) for fornecida
        return 0, [], []

    score = nlp_service.calculate_similarity(resume_text, target_text)
    matched, missing = nlp_service.get_keyword_gap(resume_text, target_text)

    return int(score), matched, missing

def get_match_level(score: int) -> str:
    if score >= 71:
        return "Strong match"
    elif score >= 41:
        return "Mid-level"
    else:
        return "Junior"
