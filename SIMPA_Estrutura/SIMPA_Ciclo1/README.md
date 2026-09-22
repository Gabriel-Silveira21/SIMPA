# SIMPA

Sistema Inteligente de Monitoramento e Planejamento Acadêmico.

Projeto Integrador do curso de Inteligência Artificial.

## Estrutura do Ciclo 1

- `frontend/templates/` — páginas HTML, incluindo `index.html`.
- `frontend/static/` — estilos CSS, incluindo `style.css`.
- `frontend/components/` — componentes da interface, quando necessários.
- `backend/classes/` — classes orientadas a objetos: Aluno, Turma, Usuário, Disciplina, Nota e Indicador.
- `backend/api/` — rotas GET, POST, PUT e DELETE e testes da API.
- `backend/database/` — banco SQLite, tabelas, integração e CRUD.
- `uml/` — diagramas de Casos de Uso e Classes.
- `tests/` — testes do projeto e da API.
- `docs/` — documentação, arquitetura, fluxogramas, pseudocódigo e materiais da apresentação.

## Divisão do projeto — 7 pessoas

1. **Gabriel — Líder do Projeto / Integração**
   - Estrutura do projeto
   - Configuração do Flask
   - Integração frontend + backend + API
   - Teste da aplicação final
   - Execução no navegador

2. **Desenvolvedor Frontend (HTML)**
   - Página principal
   - Campo de pergunta
   - Botão de envio
   - Área de resposta
   - `frontend/templates/index.html`

3. **Desenvolvedor de Estilo (CSS)**
   - Layout
   - Cores
   - Organização dos elementos
   - Aparência da aplicação
   - `frontend/static/style.css`

4. **Desenvolvedor da API de IA**
   - Integração com a API da OpenAI
   - Envio da pergunta
   - Recebimento da resposta
   - `services/ia_service.py`

5. **Engenheiro de Prompt (IA)**
   - Comportamento do assistente
   - Criação dos prompts
   - Contexto acadêmico das respostas

6. **Desenvolvedor Backend Flask**
   - Rotas Flask
   - Recebimento da pergunta do HTML
   - Comunicação com a IA
   - Retorno da resposta
   - `app.py`

7. **Documentação / Arquitetura**
   - Fluxograma
   - Pseudocódigo
   - Arquitetura do sistema
   - Slides da apresentação
   - draw.io, Canva e Google Slides

## Fluxo de trabalho no GitHub

Cada integrante deve trabalhar em uma branch própria e abrir um Pull Request para `main`.
A branch `main` deve receber somente alterações revisadas e integradas.

## Branches sugeridas

- `feature/frontend-html`
- `feature/frontend-css`
- `feature/ia-api`
- `feature/prompt`
- `feature/backend-flask`
- `feature/documentacao`

A branch `main` fica sob integração do líder do projeto.
