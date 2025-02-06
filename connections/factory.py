# connections/factory.py
from connections.chatgpt_connection import ChatGPTConnection
from connections.bert_connection import BERTConnection
from connections.api_connection import APIConnection

class APIConnectionFactory:
    @staticmethod
    def get_connection(model_name: str):
        if model_name == "chatgpt":
            return ChatGPTConnection()
        elif model_name == "bert":
            return BERTConnection()  # Agora instanciando corretamente o BERTConnection
        else:
            raise ValueError(f"Modelo '{model_name}' não encontrado.")
