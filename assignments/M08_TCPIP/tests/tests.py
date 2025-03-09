import unittest
import socket
import random
from helpers import *
import os 
import time
import multiprocessing as mp

#Never do following! The test process can be halted by student code!
#from my_code import *

import platform
import threading

use_fork=False

started_tests = 0
completed_tests = 0

succeed=0

def client_main(idx):
    global succeed
    localIP="127.0.0.1"
    serverPort=7537
    buffSize=1024

    TCPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    TCPSocket.connect((localIP, serverPort))

    N=random.randrange(3, 10)
    rnd=random.sample(range(-30, 30), N)
    total=0
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
        #print('Received:', msg1)

        total=total+r
        assert int(msg1)==total
        
    print('Close socket')
    TCPSocket.close()

    print('Got sum:'+msg1+'. Value shall be '+str(sum(rnd))+', sent data='+str(rnd))
    
    assert int(msg1)==sum(rnd)
    print('Test client '+str(idx)+' passed!')
    succeed=succeed+1

class TestCode(unittest.TestCase):
    def run_clients(self):
        time.sleep(3)
        client_list=[]
        for idx in range(20):
            th=threading.Thread(target=client_main, args=(idx,))
            th.start()
            client_list.append(th)

        for c in client_list:
            c.join()

        client_list=[]
        for idx in range(5):
            th=threading.Thread(target=client_main, args=(idx+20,))
            th.start()
            client_list.append(th)

        for c in client_list:
            c.join()

        global succeed
        print(succeed, 'succesfully served clients, shall be 25!')
        self.assertTrue(succeed>=25)
        print('\n\nNOTE:Client process tests completed succesfully. This is the only test that matters on this assignment.\n\n')
        

    def test_Python(self):
        if (platform.system()!='Windows') and use_fork:
            print('Use fork() to create subprocesses!')
            pid=os.fork()

            if pid!=0: #Parent
                self.startTest()
                self.run_clients()
                self.endTest()
                print('Wait server to exit')
                time.sleep(3)
            else:
                #Forked process, start student server
                callpython(timeout=5)
                #Time.sleep(20)
                print('Server completed!')
                #time.sleep(1)
                #print('\n\nNOTE:Server process tells that \'0 tests completed succesfully\', don\'t worry!\n\n')
                os._exit(os.EX_OK)
        else:
            print('Use multiprocessing to create subprocesses!')
            print('Start server...')
            #mp.set_start_method('spawn')
            p=callpython_subprocess(timeout=5)
            #p.start()
            time.sleep(1)
            print('Start Clients...')
            self.startTest()
            self.run_clients()
            time.sleep(1)
            self.endTest()
            for cp in mp.active_children():
                print(cp)
            
            #p.terminate()
            #p.kill()
            p.join()
            #print(p)
            
    def startTest(self):
        global started_tests
        started_tests=started_tests+1
        print('\nStart test', started_tests)

    def endTest(self):
        global completed_tests
        print('End test', started_tests)
        completed_tests=completed_tests+1


def completed():
    global completed_tests
    return completed_tests

def started():
    global started_tests
    return started_tests

