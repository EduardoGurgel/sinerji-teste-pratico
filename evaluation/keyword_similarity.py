# evaluation/keyword_similarity.py
from evaluation.evaluation_strategy import EvaluationStrategy

class KeywordSimilarity(EvaluationStrategy):
    """Avalia a resposta com base na similaridade de palavras-chave."""

    def evaluate(self, user_question: str, model_response: str) -> float:
        user_keywords = set(user_question.lower().split())
        response_keywords = set(model_response.lower().split())

        if not user_keywords:
            return 0.0

        similarity = len(user_keywords.intersection(response_keywords)) / len(user_keywords)
        return round(similarity * 100, 2)  
