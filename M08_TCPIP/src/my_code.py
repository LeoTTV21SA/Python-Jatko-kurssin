import socket
import sys
import threading
import random

localIP="127.0.0.1"
serverPort=7537
buffSize=1024


#Write your code here!


#You can utilize following client for test purposes
def client_main():
    TCPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    TCPSocket.connect((localIP, serverPort))

    rnd=random.sample(range(-30, 30), 5)
    for r in rnd:
        msg=str(r)
        print('Send:', msg)
        bytesToSend=str.encode(msg)

        TCPSocket.send(bytesToSend)

        #print('Wait message')
        data=TCPSocket.recv(buffSize)
        data=data.decode()
        data=data.splitlines()
        msg1=data[0]
        print('Received:', msg1)

    print('Close socket')
    TCPSocket.close()

    print('Got sum:'+msg1+'. Value shall be '+str(sum(rnd))+', sent data='+str(rnd))
    
    assert int(msg1)==sum(rnd)
    print('Test passed!')



#Set True to run the clients
run_client=False

if run_client:
    th_list=[]
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
