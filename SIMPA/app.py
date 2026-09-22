from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

from services.ia_service import perguntar_ia

load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    resposta = None
    pergunta = ""

    if request.method == "POST":
        pergunta = request.form.get("pergunta", "").strip()

        if pergunta:
            resposta = perguntar_ia(pergunta)
        else:
            resposta = "Digite uma pergunta para continuar."

    return render_template(
        "index.html",
        pergunta=pergunta,
        resposta=resposta
    )


@app.route("/api/perguntar", methods=["POST"])
def api_perguntar():
    dados = request.get_json(silent=True) or {}
    pergunta = str(dados.get("pergunta", "")).strip()

    if not pergunta:
        return jsonify({"erro": "A pergunta não pode estar vazia."}), 400

    resposta = perguntar_ia(pergunta)

    return jsonify({
        "pergunta": pergunta,
        "resposta": resposta
    })


if __name__ == "__main__":
    app.run(debug=True)
