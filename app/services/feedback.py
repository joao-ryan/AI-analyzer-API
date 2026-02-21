from typing import List, Tuple

def generate_feedback(score: int, missing_keywords: List[str], matched_keywords: List[str]) -> Tuple[List[str], List[str], List[str]]:
    strengths = []
    weaknesses = []
    suggestions = []

    # Feedback de Pontuação de Força
    if score >= 71:
        strengths.append(f"Excelente alinhamento com o cargo (Pontuação: {score}%)")
        strengths.append("Alta densidade de palavras-chave técnicas relevantes")
    elif score >= 41:
        strengths.append("Alinhamento moderado com os requisitos da vaga")
        weaknesses.append("Algumas habilidades técnicas importantes estão faltando no currículo")
    else:
        weaknesses.append("Baixo alinhamento com o perfil da vaga alvo")
        weaknesses.append("Falta de palavras-chave principais padrão da indústria")

    # Feedback específico de palavras-chave
    if matched_keywords:
        strengths.append(f"Forte presença de: {', '.join(matched_keywords[:5])}")

    if missing_keywords:
        weaknesses.append("Palavras-chave críticas faltando para este cargo")
        suggestions.append(f"Considere adicionar estas habilidades se você tiver experiência com elas: {', '.join(missing_keywords[:5])}")

    # Sugestões gerais
    suggestions.append("Quantifique suas conquistas (ex: 'Reduzi custos em 20%')")
    suggestions.append("Certifique-se de que suas informações de contato e perfil do LinkedIn estejam atualizados")
    suggestions.append("Personalize seu resumo para destacar experiências específicas relevantes para o cargo")

    return strengths, weaknesses, suggestions
