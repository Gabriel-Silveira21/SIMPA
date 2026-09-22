# Contribuindo com o SIMPA

## Branches

- `main` → versão estável.
- `develop` → integração das funcionalidades.
- `feature/gabriel` → liderança e integração.
- `feature/frontend` → HTML.
- `feature/css` → CSS.
- `feature/ia-api` → integração da API de IA.
- `feature/prompt` → engenharia de prompt.
- `feature/backend` → backend Flask.
- `feature/documentacao` → documentação e arquitetura.

## Regra principal

Não faça commits diretamente na `main`.

Fluxo:

```text
feature/nome
     |
     v
 Pull Request
     |
     v
  develop
     |
     v
   testes
     |
     v
    main
```

## Antes de começar

```bash
git checkout develop
git pull origin develop
git checkout feature/sua-branch
```

## Commit

Utilize mensagens objetivas:

```text
feat: adiciona campo de pergunta
fix: corrige envio do formulário
style: ajusta layout
docs: atualiza arquitetura
refactor: reorganiza serviço da IA
```

## Enviar alterações

```bash
git add .
git commit -m "feat: descrição da alteração"
git push origin feature/sua-branch
```

Depois, abra um Pull Request para `develop`.

## Arquivos sensíveis

Nunca envie:

- `.env`
- chaves de API
- senhas
- tokens
- credenciais
