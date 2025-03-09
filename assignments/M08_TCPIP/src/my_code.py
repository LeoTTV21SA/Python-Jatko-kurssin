import socket
import sys
import threading
import random

localIP = "127.0.0.1"
serverPort = 7537
buffSize = 1024

client_count = 0
count_lock = threading.Lock()

def handle_client(client_socket, addr):
    global client_count
    total = 0
    try:
        while True:
            data = client_socket.recv(buffSize)
            if not data:
                break
            number = int(data.decode().strip())
            total += number
            response = str(total) + "\n"
            client_socket.send(response.encode())
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        with count_lock:
            client_count += 1
        client_socket.close()
        print(f"Client {addr} disconnected. Total clients served: {client_count}")

def server_main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Permitir reutilización del puerto
    server_socket.bind((localIP, serverPort))
    server_socket.listen(25)
    print(f"Server listening on {localIP}:{serverPort}")
    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"New connection from {addr}")
            client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
            client_thread.start()
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()

# Resto del código (client_main, if __name__ == "__main__") permanece igual
if __name__ == "__main__":
    server_thread = threading.Thread(target=server_main)
    server_thread.start()
    server_thread.join()