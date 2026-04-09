import socket
import threading

HOST = '0.0.0.0'
PORT = 10396

def handle_client(conn, addr):
    try:
        # recebe nome do cliente logo na conexão
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

            # resposta automática (melhor pra múltiplos clientes)
            resposta = f"Servidor recebeu: {mensagem}"
            conn.send(resposta.encode())

    except Exception as e:
        print(f"Erro com {addr}: {e}")

    finally:
        conn.close()

# servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()

print(f"Servidor rodando na porta {PORT}...")

while True:
    conn, addr = servidor.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()