# Сервер
import socket
import threading

def handle_client(client_socket):
    # Получаем данные от клиента
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print("Received from client:", data.decode())
            # Отправляем ответ клиенту
            client_socket.sendall(data)
        except Exception as e:
            print(f"Error handling client: {e}")
            break
    # Закрываем соединение с клиентом
    client_socket.close()

def start_server():
    host = '127.0.0.1'
    port = 8000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server started on {host}:{port}")
    
    while True:
        client_socket, address = server_socket.accept()
        print(f"Client connected: {address}")
        # Создаем новый поток для обработки клиента
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
