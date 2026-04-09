import socket

HOST = '0.0.0.0'
PORT = 10396

# cria servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()

print(f"Servidor rodando na porta {PORT}...")

while True:
    print("Aguardando conexão...")

    conn, addr = servidor.accept()
    print(f"Conectado com {addr}")

    # recebe nome do cliente
    nome = conn.recv(1024).decode()
    print(f"[NOVA CONEXÃO] {nome} conectado de {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break

        mensagem = data.decode()

        if mensagem.upper() == "QUIT":
            print(f"[SAIU] {nome} ({addr}) saiu do chat.")
            break

        print(f"[{nome} - {addr}] -> {mensagem}")

        resposta = f"Servidor recebeu: {mensagem}"
        conn.send(resposta.encode())

    conn.close()
    print("Conexão encerrada.\n")