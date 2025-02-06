# connections/bert_connection.py
from connections.api_connection import APIConnection
from transformers import BertForSequenceClassification, BertTokenizer
import torch

class BERTConnection(APIConnection):
    def __init__(self):
        self.model = BertForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
        self.tokenizer = BertTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

    def query(self, question: str) -> str:
        try:
            inputs = self.tokenizer(question, return_tensors='pt')
            with torch.no_grad():
                outputs = self.model(**inputs)
            prediction = torch.argmax(outputs.logits, dim=1).item()
            sentiment_map = {0: 'Very negative', 1: 'Negative', 2: 'Neutral', 3: 'Positive', 4: 'Very positive'}
            return f"Sentimento do BERT: {sentiment_map[prediction]}"
        except Exception as e:
            return f"Erro ao acessar o modelo BERT: {e}"