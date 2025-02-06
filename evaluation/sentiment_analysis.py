# evaluation/sentiment_analysis.py
from evaluation.evaluation_strategy import EvaluationStrategy
from textblob import TextBlob

class SentimentAnalysis(EvaluationStrategy):
    """Avalia a resposta com base no sentimento (positividade/negatividade)."""

    def evaluate(self, user_question: str, model_response: str) -> float:
        analysis = TextBlob(model_response)
        return round(analysis.sentiment.polarity * 100, 2)  # -100 a 100
