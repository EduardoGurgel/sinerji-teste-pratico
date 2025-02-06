# commands/command.py
from connections.api_connection import APIConnection

class QueryCommand:
    def __init__(self, connection, question):
        self.connection = connection
        self.question = question

    def execute(self):
        try:
            response = self.connection.query(self.question)
            if response is None:
                return "Erro: Resposta vazia do modelo."
            return response
        except Exception as e:
            return f"Erro ao acessar API: {str(e)}"
