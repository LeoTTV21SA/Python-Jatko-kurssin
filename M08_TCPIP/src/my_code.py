import socket
import sys
import threading
import random

localIP = "127.0.0.1"
serverPort = 7537
buffSize = 1024

# Contador de clientes atendidos y candado para thread-safety
client_count = 0
count_lock = threading.Lock()

def handle_client(client_socket, addr):
    # Käsittele yksittäisen asiakkaan pyynnöt
    global client_count
    total = 0
    
    try:
        while True:
            # Vastaanota dataa asiakkaalta
            data = client_socket.recv(buffSize)
            if not data:
                break  # Asiakas sulki yhteyden
            
            # Muunna vastaanotettu data numeroksi ja laske summa
            number = int(data.decode().strip())
            total += number
            
            # Lähetä nykyinen summa takaisin asiakkaalle
            response = str(total) + "\n"
            client_socket.send(response.encode())
    
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    
    finally:
        # Päivitä asiakaslaskuri turvallisesti ja sulje yhteys
        with count_lock:
            global client_count
            client_count += 1
        client_socket.close()
        print(f"Client {addr} disconnected. Total clients served: {client_count}")

def server_main():
    # Luo TCP-palvelinsoketti
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((localIP, serverPort))
    server_socket.listen(25)  # Sallii jopa 25 yhteyttä jonossa
    
    print(f"Server listening on {localIP}:{serverPort}")
    
    try:
        while True:
            # Hyväksy asiakasyhteys
            client_socket, addr = server_socket.accept()
            print(f"New connection from {addr}")
            
            # Käynnistä uusi säie asiakkaan käsittelyyn
            client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
            client_thread.start()
            
            # Tarkista, onko 25 asiakasta käsitelty
            with count_lock:
                if client_count >= 25:
                    print("Served 25 clients, shutting down server")
                    break
    
    finally:
        server_socket.close()

#Write your code here!

#You can utilize following client for test purposes
def client_main():
    TCPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    TCPSocket.connect((localIP, serverPort))

    rnd = random.sample(range(-30, 30), 5)
    for r in rnd:
        msg = str(r)
        print('Send:', msg)
        bytesToSend = str.encode(msg)

        TCPSocket.send(bytesToSend)

        #print('Wait message')
        data = TCPSocket.recv(buffSize)
        data = data.decode()
        data = data.splitlines()
        msg1 = data[0]
        print('Received:', msg1)

    print('Close socket')
    TCPSocket.close()

    print('Got sum:' + msg1 + '. Value shall be ' + str(sum(rnd)) + ', sent data=' + str(rnd))
    
    assert int(msg1) == sum(rnd)
    print('Test passed!')

#Set True to run the clients
run_client = False

if __name__ == "__main__":
    # Käynnistä palvelin pääohjelmassa
    server_thread = threading.Thread(target=server_main)
    server_thread.start()

    if run_client:
        th_list = []
        for i in range(20):
            th_list.append(threading.Thread(target=client_main))
            th_list[-1].start()

        for th in th_list:
            th.join()

        for i in range(5):
            th_list.append(threading.Thread(target=client_main))
            th_list[-1].start()

        for th in th_list:
            th.join()

        #After 25 clients the server shall exit
    server_thread.join()