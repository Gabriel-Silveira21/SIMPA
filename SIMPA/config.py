import os

# Configurações centralizadas do projeto.
# Valores sensíveis devem ficar no arquivo .env.

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5")
