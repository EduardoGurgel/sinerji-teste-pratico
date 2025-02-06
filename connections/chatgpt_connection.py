# connections/chatgpt_connection.py
import openai
import os
from connections.api_connection import APIConnection

class ChatGPTConnection(APIConnection):
    def __init__(self):
        # Define a chave de API a partir de uma variável de ambiente
        openai.api_key = os.getenv("OPENAI_API_KEY")
        if not openai.api_key:
            raise ValueError("A variável de ambiente OPENAI_API_KEY não está definida.")

    def query(self, question: str) -> str:
        """Método para enviar a pergunta e obter a resposta do ChatGPT"""
        try:
            # Envio da pergunta para a API do ChatGPT
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # ou outro modelo como "gpt-4"
                messages=[{"role": "user", "content": question}],
            )
            
            # Extrai a resposta da API
            message = response['choices'][0]['message']['content'].strip()  # Corrigido para a estrutura atual
            return message
        except Exception as e:
            return f"Erro ao acessar a API: {e}"
