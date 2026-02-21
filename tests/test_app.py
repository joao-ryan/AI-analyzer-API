from fastapi.testclient import TestClient
from app.main import app
from app.services.scorer import calculate_score

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_roles():
    response = client.get("/api/roles")
    assert response.status_code == 200
    assert "Software Engineer" in response.json()["roles"]

def test_scoring_logic():
    resume = "Eu sou um desenvolvedor Python com experiência em FastAPI e Docker."
    role = "Backend Developer"
    score, matched, missing = calculate_score(resume, role)

    assert score > 0
    assert "python" in [m.lower() for m in matched] or "fastapi" in [m.lower() for m in matched]

def test_analyze_endpoint_text():
    response = client.post(
        "/api/analyze",
        data={
            "resume_text": "Experienced Frontend Developer with React and TypeScript skills.",
            "job_role": "Frontend Developer"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "score" in data
    assert "match_level" in data
    assert len(data["feedback"]["strengths"]) > 0
