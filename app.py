import os

from flask import Flask, request, jsonify, render_template

from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def carregar_informacoes():
    with open('informacoes.txt', 'r', encoding='utf-8') as f:
        return f.read()

contexto_informacoes = carregar_informacoes()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    pergunta = request.json.get('pergunta')
    resposta = obter_resposta(pergunta)
    return jsonify({"resposta": resposta})

def obter_resposta(pergunta):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": contexto_informacoes},
                {"role": "user", "content": pergunta}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Erro ao acessar a API do OpenAI: {e}")
        return "Desculpe, ocorreu um erro ao processar sua pergunta."

if __name__ == "__main__":
    app.run(debug=True)
