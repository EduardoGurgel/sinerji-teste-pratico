# evaluation/response_evaluator.py
from evaluation.keyword_similarity import KeywordSimilarity
from evaluation.sentiment_analysis import SentimentAnalysis

class ResponseEvaluator:
    """Classe que aplica uma estratégia de avaliação."""

    def __init__(self, strategy):
        self.strategy = strategy

    def evaluate(self, user_question: str, model_response: str) -> float:
        return self.strategy.evaluate(user_question, model_response)

    def set_strategy(self, strategy):
        self.strategy = strategy
