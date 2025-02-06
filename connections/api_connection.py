# connections/api_connection.py
from abc import ABC, abstractmethod

class APIConnection(ABC):
    @abstractmethod
    def query(self, question: str) -> str:
        """Método abstrato para enviar a consulta à API e retornar a resposta"""
        pass
