# Arquitetura do SIMPA

## Visão inicial

O SIMPA é organizado em camadas simples:

```text
Usuário
   |
   v
Frontend (HTML/CSS/JS)
   |
   v
Flask (app.py)
   |
   v
Serviço de IA (ia_service.py)
   |
   v
Prompt (prompt_service.py)
   |
   v
API de Inteligência Artificial
```

## Responsabilidades

- `templates/index.html`: estrutura da interface.
- `static/css/style.css`: aparência e layout.
- `static/js/script.js`: interações do navegador.
- `app.py`: rotas e integração.
- `services/ia_service.py`: comunicação com a API de IA.
- `services/prompt_service.py`: instruções do assistente.
- `docs/`: documentação técnica do projeto.
