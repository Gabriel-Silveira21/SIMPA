# SIMPA

## Assistente Acadêmico

O SIMPA é um projeto acadêmico de um assistente voltado ao apoio de alunos
em dúvidas relacionadas a aulas, provas, estudos e conteúdos educacionais.

## Estrutura

```text
SIMPA/
│
├── app.py
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── img/
│
├── services/
│   ├── __init__.py
│   ├── ia_service.py
│   └── prompt_service.py
│
├── docs/
│   ├── arquitetura.md
│   ├── fluxograma.md
│   └── pseudocodigo.md
│
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

## Equipe e responsabilidades

| Área | Branch | Principal responsabilidade |
|---|---|---|
| Gabriel / Integração | `feature/gabriel` | Estrutura e integração |
| Frontend | `feature/frontend` | HTML |
| CSS | `feature/css` | Estilo |
| API da IA | `feature/ia-api` | Comunicação com a IA |
| Prompt | `feature/prompt` | Comportamento do assistente |
| Backend | `feature/backend` | Flask e rotas |
| Documentação | `feature/documentacao` | Arquitetura e documentação |

## Instalação

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
cd SIMPA
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

No Windows:

```bash
venv\Scripts\activate
```

No Linux/macOS:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie o arquivo `.env`:

```text
.env.example → .env
```

Depois preencha:

```env
OPENAI_API_KEY=sua_chave
OPENAI_MODEL=gpt-5
```

Execute:

```bash
python app.py
```

Abra no navegador o endereço mostrado pelo Flask.

## Fluxo Git

```text
main
  ^
  |
develop
  ^
  |
feature/nome
```

Cada integrante deve trabalhar na sua própria branch e enviar Pull Requests
para `develop`.

## Segurança

Nunca publique chaves de API, senhas ou arquivos `.env`.

## Licença

Consulte o arquivo `LICENSE`.
