# Atividade 2 - Chat Cliente/Servidor

## 📌 Descrição

Esta atividade consiste na implementação de um chat simples entre cliente e servidor utilizando sockets TCP em Python.

A aplicação permite a troca de mensagens entre cliente e servidor até que uma das partes envie o comando `QUIT`, encerrando a comunicação.

Diferente da atividade 3, esta versão atende apenas **um cliente por vez**, sem uso de threads.

---

## 📁 Arquivos

* `cliente.py`: responsável por conectar ao servidor, enviar mensagens e receber respostas.
* `servidor.py`: responsável por aceitar a conexão de um cliente, receber mensagens e responder.

---

## ⚙️ Como executar

1. Acesse a pasta:

```bash
cd atividade-2-chat
```

2. Execute o servidor:

```bash id="srv2"
python servidor.py
```

3. Em outro terminal:

```bash id="cli2"
python cliente.py
```

---

## 🔌 Porta utilizada

10396

---

## ⚡ Funcionalidades

* Comunicação cliente-servidor via TCP
* Envio e recebimento de mensagens
* Identificação do cliente por nome
* Encerramento da conexão com comando `QUIT`
* Atendimento de um cliente por vez

---

## 🔄 Fluxo da aplicação

1. O servidor é iniciado e fica aguardando conexão
2. O cliente se conecta ao servidor
3. O cliente informa seu nome
4. O cliente envia mensagens
5. O servidor recebe, exibe no terminal e responde
6. A comunicação continua até o envio de `QUIT`
7. A conexão é encerrada

---

## 🧠 Lógica da aplicação

* O servidor fica em modo de escuta (`listen`) aguardando conexões
* Ao conectar, o cliente envia seu nome
* O servidor recebe mensagens e responde automaticamente
* A comunicação é contínua até que o comando `QUIT` seja enviado

---

## 🛠️ Requisitos

* Python 3.x
* Terminal ou IDLE

---

## 📌 Observações

* O servidor deve ser executado antes do cliente
* Cliente e servidor devem utilizar a mesma porta (10396)
* O servidor atende um cliente por vez (sem threads)
* Caso o cliente seja executado antes do servidor, a conexão não será estabelecida
* A comunicação termina ao enviar `QUIT`

* link do video: https://youtu.be/pr4VtOFqnpk?si=DsPHngd1BOrwOhY7
