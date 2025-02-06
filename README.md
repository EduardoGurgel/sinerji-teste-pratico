# Projeto: Comparador de Modelos de IA (ChatGPT e BERT)

## 📌 Descrição
Este projeto tem como objetivo conectar-se a modelos de IA como **ChatGPT** e **BERT**, utilizando **padrões de projeto**. Ele permite enviar perguntas para os modelos e avaliar as respostas com diferentes critérios.

---
Vídeo (Youtube): https://youtu.be/REzBpWuw0S8
## 🚀 Configuração do Ambiente
Para rodar o projeto localmente, siga os passos abaixo:

### 1️⃣ **Clonar o Repositório**
```bash
git clone git@github.com:EduardoGurgel/sinerji-teste-pratico.git
cd sinerji-teste-pratico
```

### 2️⃣ **Criar e Ativar um Ambiente Virtual (venv)**
#### No Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
#### No Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ **Instalar as Dependências**
Após ativar o ambiente virtual, instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

---

## 🔑 Configuração da API Key do OpenAI
Para utilizar o ChatGPT, é necessário definir a variável de ambiente `OPENAI_API_KEY`.

### No Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="sua-chave-aqui"
```

### No Linux/Mac (Terminal):
```bash
export OPENAI_API_KEY="sua-chave-aqui"
```

> **OBS:** Substitua `sua-chave-aqui` pela chave obtida no site da [OpenAI](https://platform.openai.com/).

---

## ▶️ Como Executar o Projeto
Após configurar tudo, rode o projeto com:
```bash
python main.py
```
O sistema pedirá que você escolha o modelo de IA (ChatGPT ou BERT) e permitirá fazer perguntas. Em seguida, aplicará estratégias de avaliação para analisar a resposta.

---

## 🏗️ Padrões de Projeto Utilizados
- **Factory**: Para instanciar dinamicamente diferentes conexões com APIs.
- **Command**: Para encapsular as requisições como objetos reutilizáveis.
- **Strategy**: Para definir e trocar critérios de avaliação das respostas.
- **Observer**: Para permitir notificações e atualizações automáticas

---

## 📩 Contato
Caso tenha dúvidas ou sugestões, entre em contato:
- Email: eduardo-gurgel@hotmail.com
- Telefone: (61) 9 8123-6435
