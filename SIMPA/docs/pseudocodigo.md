# Pseudocódigo

```text
INÍCIO

Usuário acessa o SIMPA

MOSTRAR tela principal

Usuário digita uma pergunta

SE pergunta estiver vazia
    mostrar mensagem de erro
SENÃO
    enviar pergunta para o Flask

    Flask chama o serviço de IA

    serviço aplica o prompt

    serviço envia a pergunta para a API

    receber resposta

    devolver resposta para o Flask

    mostrar resposta ao usuário
FIM SE

FIM
```
