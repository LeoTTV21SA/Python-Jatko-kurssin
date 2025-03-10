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


#from my_code import fetch_number

server_running=True

def server_main():
    UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPSocket.bind(("127.0.0.1", 7938))
    print('Test UDP server up and listening')

    global server_running
    while server_running:
        UDPSocket.settimeout(10)
        try:
            bytesAddressPair = UDPSocket.recvfrom(1024)
        except:
            print('UDPSocket.recvfrom(1024) - exception!')
            server_running=False
            
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]

        message=message.decode()
        #print(message)

        if message=='Anna luku!': 
            ret=random.randint(-10, 10)
            message=str(ret).encode()
            UDPSocket.settimeout(10)
            try:
                #print(f'Send {message} {address}')
                UDPSocket.sendto(message, address)
                #print(f'sent {ret}')
            except:
                print('UDPSocket.sendto(message, address) - exception')
                server_running=False
            #print(str(address)+' : '+str(maxValue)+' : '+str(ret))

ct_count=0
ct_count_lock=threading.Lock()
            
def client_thread():
    global ct_count

    fetch_number("127.0.0.1", 7938)

    with ct_count_lock:
        ct_count=ct_count+1
            
class TestCode(unittest.TestCase):
    """
    def run_clients(self):
        time.sleep(3)
        client_list=[]
        for idx in range(20):
            th=threading.Thread(target=client_thread)
            th.start()
            client_list.append(th)

        time.sleep(1)

        with ct_count_lock:
            #print(f'ct_count = {ct_count}')
            assert ct_count>=19
        print('Client multithreading test completed')
    """  

    def test_Python(self):
        self.startTest()
        print('Use multiprocessing to create subprocesses!')
        print('Start server...')
        p=mp.Process(target=server_main)
        p.start()
        time.sleep(1)
        print('Server running...')

        #print('Start multithread testing...')
        #self.run_clients()
        #print('...Completed')

        print('Check return values...')
        test_code="""
import sys
sys.path.insert(0, '../src')

from my_code import fetch_number

rc_list=[]
for idx in range(100):
    rc=fetch_number("127.0.0.1", 7938)
    rc_list.append(rc)
    #print(idx, rc)

constant=True
in_range=True
for rc in rc_list:
    if rc!=rc_list[0]:
        constant==False
    if rc<-10 or rc>10:
        inrange=False 

assert constant==True
assert in_range==True

print('fetch_number text completed')
"""
        print('callpythoncode started')
        ret=callpythoncode(test_code, timeout=15)
        print(ret)
        print('callpythoncode complete')

        #Kill the server
        server_running=False
        p.kill()
        self.assertTrue('completed' in ret)
        print('...Completed')
        
        time.sleep(1)
        self.endTest()
            
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

