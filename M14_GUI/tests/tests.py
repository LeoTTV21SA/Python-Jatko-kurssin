import unittest
from helpers import *

#Comment out if no python functions are tested
#NOTE: If this is not commented out, src/my_code.py will be executed.
#(You can abuse this, for example, if you like to check global variables etc.)
#from my_code import *

started_tests = 0
completed_tests = 0

code="""
import sys
sys.path.insert(0, '../src')
import my_code

my_code.init_mainloop()

def mymainloop():
    print('Enter mainloop()')
    while my_code.active_mainloop:
        k=input('***')
        print(k)
        if k!='':
            if k in my_code.events:
                f=my_code.events[k]
                f()
            else:
                print(f'"{k}" not found from events list!')
    print('Exit mainloop()')

mymainloop()

"""

class TestCode(unittest.TestCase):
    def test_Python(self):
        #Test python program
        self.startTest()
        res=callpythoncode(code=code, cmdline_args=[], input='m\n82364876238476\nm\nm\nm\nm\nm\nm\nm\nm\nm\nr\n8\nx\n', timeout=10)
        print(res)
        must_include=['***', 'Exit mainloop()', 'Hello World!" have been printed 10 times!', '"82364876238476" not found from events list!', 'Number of empty rows:', 8*'\n', 'Hello World!" have been printed 1 times!']
        for txt in must_include:
            print('Test if output contains "'+txt+'"', end=' ')
            self.assertTrue(txt in res)
            print('- ok')
        must_not_include=[16*'\n', 'Hello World!" have been printed 11 times!']
        for txt in must_not_include:
            print('Test if output does not contain "'+txt+'"', end=' ')
            self.assertTrue(txt not in res)
            print('- ok')


        res=callpythoncode(code=code, cmdline_args=[], input='r\n16\nm\nx\n', timeout=10)
        print(res)
        must_include=['***', 'Exit mainloop()', 'Number of empty rows:', 16*'\n', 'Hello World!" have been printed 1 times!']
        for txt in must_include:
            print('Test if output contains "'+txt+'"', end=' ')
            self.assertTrue(txt in res)
            print('- ok')
        must_not_include=['10', 'not found']
        for txt in must_not_include:
            print('Test if output does not contain "'+txt+'"', end=' ')
            self.assertTrue(txt not in res)
            print('- ok')

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

