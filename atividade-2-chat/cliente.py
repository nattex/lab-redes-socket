import socket

HOST = '127.0.0.1'
PORT = 10396

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

nome = input("Digite seu nome: ")
cliente.send(nome.encode())

while True:
    mensagem = input("Você: ")
    cliente.send(mensagem.encode())

    if mensagem.upper() == "QUIT":
        break

    resposta = cliente.recv(1024).decode()
    print("Servidor:", resposta)

cliente.close()