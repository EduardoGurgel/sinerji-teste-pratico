# evaluation/evaluation_strategy.py
from abc import ABC, abstractmethod

class EvaluationStrategy(ABC):
    """Interface para estratégias de avaliação de respostas."""
    
    @abstractmethod
    def evaluate(self, user_question: str, model_response: str) -> float:
        pass
