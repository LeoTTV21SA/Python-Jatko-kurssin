import socket
import sys
import threading
import random
import time

localIP = "127.0.0.1"
serverPort = 7538
buffSize = 1024

def server_main():
    # Luo UDP-palvelinsoketti
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((localIP, serverPort))
    
    print(f"Server listening on {localIP}:{serverPort}")
    
    try:
        while True:
            # Vastaanota dataa asiakkaalta
            data, addr = server_socket.recvfrom(buffSize)
            maxval = int(data.decode().strip())
            
            # Generoi satunnaisluku 0 ja maxval-1 väliltä
            response = random.randrange(0, maxval)
            
            # Lähetä vastaus takaisin asiakkaalle
            server_socket.sendto(str(response).encode(), addr)
            
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()

#Write your code here!

#You can utilize following client for test purposes
def client_main():
    UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    #No bindig => Pick random port

    for i in range(10):
        msg = str(4 + 3 * i)
        bytesToSend = str.encode(msg)
        serverAddressPort = (localIP, serverPort)
        UDPSocket.sendto(bytesToSend, serverAddressPort)
        bytesAddressPair = UDPSocket.recvfrom(buffSize)
        message = bytesAddressPair[0]

        print(msg + ' :', message.decode())
        #time.sleep(1.0)

    UDPSocket.close()

#Set True to run the clients
run_client = False

if __name__ == "__main__":
    # Käynnistä palvelin pääohjelmassa
    server_thread = threading.Thread(target=server_main)
    server_thread.start()

    if run_client:
        th_list = []
        for i in range(10):
            th_list.append(threading.Thread(target=client_main))
            th_list[-1].start()

        for th in th_list:
            th.join()
    
    server_thread.join()