from openai import OpenAI

from config import OPENAI_API_KEY, OPENAI_MODEL
from services.prompt_service import criar_prompt


def perguntar_ia(pergunta: str) -> str:
    """Envia uma pergunta para a IA e retorna o texto da resposta."""

    if not OPENAI_API_KEY:
        return (
            "A chave da API ainda não foi configurada. "
            "Crie um arquivo .env a partir do .env.example."
        )

    try:
        client = OpenAI(api_key=OPENAI_API_KEY)

        resposta = client.responses.create(
            model=OPENAI_MODEL,
            instructions=criar_prompt(),
            input=pergunta
        )

        return resposta.output_text

    except Exception as erro:
        # Evita expor detalhes internos da API ao usuário final.
        print(f"Erro na API de IA: {erro}")
        return "Não foi possível obter uma resposta no momento."
