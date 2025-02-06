# main.py
from connections.factory import APIConnectionFactory
from commands.command import QueryCommand
from evaluation.response_evaluator import ResponseEvaluator
from evaluation.keyword_similarity import KeywordSimilarity
from evaluation.sentiment_analysis import SentimentAnalysis
import nltk
from nltk.data import find

def main():
    try:
        find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
        
    print("Bem-vindo à CLI para consulta a modelos de linguagem!")
    print("Modelos disponíveis: ChatGPT e BERT")
    print("Digite 'sair' para encerrar.\n")

    try:
        chatgpt_conn = APIConnectionFactory.get_connection("chatgpt")
        bert_conn = APIConnectionFactory.get_connection("bert")
    except ValueError as e:
        print(e)
        return

    # Escolher a estratégia de avaliação
    print("\nEscolha a estratégia de avaliação:")
    print("1 - Similaridade por palavras-chave")
    print("2 - Análise de Sentimento")
    eval_choice = input("Digite sua opção [1/2]: ").strip()
    
    if eval_choice == "1":
        evaluator = ResponseEvaluator(KeywordSimilarity())
    elif eval_choice == "2":
        evaluator = ResponseEvaluator(SentimentAnalysis())
    else:
        print("Opção inválida. Usando Similaridade por palavras-chave como padrão.")
        evaluator = ResponseEvaluator(KeywordSimilarity())

    try:
        while True:
            try:
                question = input("\nDigite sua pergunta: ").strip()
            except KeyboardInterrupt:
                print("\n\nEncerrando a aplicação. Até logo!")
                break

            if question.lower() == "sair":
                print("Encerrando a aplicação. Até logo!")
                break

            print("\nEscolha o modelo para enviar a consulta:")
            print("1 - ChatGPT")
            print("2 - BERT")
            print("3 - Enviar para ambos")
            
            try:
                model_choice = input("Digite sua opção [1/2/3]: ").strip()
            except KeyboardInterrupt:
                print("\n\nEncerrando a aplicação. Até logo!")
                break
            
            commands = []
            responses = {}

            if model_choice == "1":
                commands.append(QueryCommand(chatgpt_conn, question))
            elif model_choice == "2":
                commands.append(QueryCommand(bert_conn, question))
            elif model_choice == "3":
                commands.append(QueryCommand(chatgpt_conn, question))
                commands.append(QueryCommand(bert_conn, question))
            else:
                print("Opção inválida. Tente novamente.\n")
                continue

            # Executa os comandos e armazena as respostas
            for command in commands:
                model_response = command.execute()
                responses[command.connection.__class__.__name__] = model_response

            # Avalia as respostas
            for model, response in responses.items():
                if response is None:
                    print(f"\n⚠️ Erro: O modelo {model} não retornou uma resposta válida.")
                    continue  # Pula essa resposta e continua com as outras
                
                score = evaluator.evaluate(question, response)
                print(f"\nModelo: {model}")
                print(f"Resposta: {response}")
                print(f"Avaliação: {score}%\n")

            print("\n" + "-" * 50 + "\n")

    except KeyboardInterrupt:
        print("\n\nEncerrando a aplicação. Até logo!")

if __name__ == "__main__":
    main()
