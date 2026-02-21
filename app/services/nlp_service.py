from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.utils.text_cleaner import clean_text

class NLPService:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def calculate_similarity(self, resume_text: str, jd_text: str) -> float:
        # Limpa o currículo e a descrição da vaga (JD)
        cleaned_resume = clean_text(resume_text)
        cleaned_jd = clean_text(jd_text)

        # Vetorização e cálculo de similaridade
        tfidf_matrix = self.vectorizer.fit_transform([cleaned_resume, cleaned_jd])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

        return float(similarity[0][0]) * 100

    def extract_keywords(self, text: str) -> set:
        # Extrai palavras-chave do texto limpo
        cleaned = clean_text(text)
        return set(cleaned.split())

    def get_keyword_gap(self, resume_text: str, jd_text: str):
        # Identifica palavras-chave encontradas e faltantes
        resume_keywords = self.extract_keywords(resume_text)
        jd_keywords = self.extract_keywords(jd_text)

        matched = resume_keywords.intersection(jd_keywords)
        missing = jd_keywords.difference(resume_keywords)

        return list(matched), list(missing)

nlp_service = NLPService()
