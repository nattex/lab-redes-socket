# Atividade 3 - Desafio

## 📌 Descrição

Esta aplicação consiste em um chat cliente-servidor desenvolvido utilizando sockets TCP em Python.

O sistema permite que múltiplos clientes se conectem ao servidor simultaneamente e enviem mensagens, utilizando threads para gerenciar várias conexões ao mesmo tempo.

A comunicação ocorre até que o cliente envie o comando `QUIT`, encerrando a conexão.

---

## 📁 Arquivos

* `cliente.py`: responsável por conectar ao servidor, enviar mensagens e receber respostas.
* `server.py`: responsável por aceitar conexões de múltiplos clientes, processar mensagens e responder.

---

## ⚙️ Como executar

1. Acesse a pasta:

```bash
cd atividade-3-desafio
```

2. Execute o servidor:

```bash
python server.py
```

3. Em outro terminal:

```bash
python cliente.py
```

---

## 🔌 Porta utilizada

10396

---

## ⚡ Funcionalidades

* Comunicação cliente-servidor via TCP
* Suporte a múltiplos clientes simultâneos (uso de threads)
* Envio e recebimento de mensagens
* Identificação do cliente por nome
* Encerramento da conexão com comando `QUIT`

---

## 🔄 Fluxo da aplicação

1. O servidor é iniciado e aguarda conexões
2. O cliente se conecta ao servidor
3. O usuário informa seu nome
4. O cliente envia mensagens
5. O servidor recebe, processa e responde
6. A comunicação continua até o envio de `QUIT`

---

## 🛠️ Requisitos

* Python 3.x
* Terminal ou IDLE

---

## 📌 Observações

* O servidor deve ser executado antes do cliente
* Cliente e servidor devem utilizar a mesma porta (10396)
* A aplicação utiliza threads para suportar múltiplos clientes
* Caso o cliente seja executado antes do servidor, a conexão não será estabelecida

---

link:  https://youtu.be/mn1JySiFUfA
link do funcionamento: https://youtu.be/ddCOIDAAptY
