# Laboratório de Redes - Socket

Repositório com os códigos das atividades 2 e 3 da disciplina de Redes de Computadores.

---

## 👥 Integrantes
- [Natália de Fátima Teixera] - [RA: 10395853]
- [Pablo Borba Leal] - [RA: 10396351]
- [Pedro Albuquerque Potiens] - [RA: 10323134]

---

## 🎯 Objetivo de cada atividade

### 💬 Atividade 2 - Chat cliente/servidor

Implementar a comunicação básica entre cliente e servidor utilizando sockets TCP, permitindo a troca de mensagens até o encerramento com o comando `QUIT`.

---

### 🚀 Atividade 3 - Desafio

Expandimos a implementação básica do chat cliente-servidor para permitir o atendimento de múltiplos clientes simultaneamente, utilizando threads no servidor.

---

## 🔍 Principais diferenças entre as atividades

* **Atividade 2:** servidor simples, atende um cliente por vez
* **Atividade 3:** servidor com threads, atende múltiplos clientes simultaneamente
* **Atividade 2:** foco na comunicação básica
* **Atividade 3:** foco em concorrência e múltiplas conexões


---

## 📁 Estrutura do repositório

```text
lab-redes-socket/
├── atividade-2-chat/
│   ├── cliente.py
│   ├── servidor.py
│   └── README.md
├── atividade-3-desafio/
│   ├── cliente.py
│   ├── server.py
│   └── README.md
└── README.md
