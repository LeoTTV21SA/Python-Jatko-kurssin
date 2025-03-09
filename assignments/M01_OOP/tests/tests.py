import unittest
from helpers import *

#Never do following! The test process can be halted by student code!
#from my_code import *



started_tests = 0
completed_tests = 0

class TestCode(unittest.TestCase):
    """
    def test_Python(self):
        #Test python program
        self.startTest()
        self.assertEqual(callpython(cmdline_args=['a', 'b'], input='\n').strip(), 'a b')
        self.endTest()
    """
    def test_PythonFunction(self):
        #Test python function (in this case function name is combine)
        #Test code (my_code) must be implemented
        self.startTest()

        expected_output=[
            'Constructor: Negative parameter generates an exception.',
            '124+19=133', '124*19=26',
            '124+0=124', '124*0=0',
            '124+1=125', '124*1=4',
            '19+124=133', '19*124=26',
            '0+124=124', '0*124=0',
            '1+124=125', '1*124=4',
            '19+124+1=134', '(19+124)*1=3',
            'Type of NumericString(1) is ok',
            'Type of NumericString(1)+NumericString(124) is ok',
            'Type of NumericString(1)*NumericString(124) is ok',
        ]
        
        my_code="""
import sys
sys.path.insert(0, '../src')

from my_code import NumericString


if True:
    o16=NumericString(16)
    try:
        print('Initializing with negative integer...', end=' ')
        o_exception=NumericString(-1)
        got_exception=False
    except:
        got_exception=True

    assert got_exception
    print('Constructor: Negative parameter generates an exception.')
    
    o124=NumericString(124)
    o19=NumericString(19)
    o0=NumericString(0)
    o1=NumericString(1)

    def test(o1, o2, expected_value1, expected_value2):
        res1=str(o1+o2)
        print(str(o1)+'+'+str(o2)+'='+res1)
        assert res1==expected_value1
        res2=str(o1*o2)
        print(str(o1)+'*'+str(o2)+'='+res2)
        assert res2==expected_value2
        
    #Test results of addition and multiplication
    test(o124, o19, '133', '26')
    test(o124, o0, '124', '0')
    test(o124, o1, '125', '4')

    test(o19, o124, '133', '26')
    test(o0, o124, '124', '0')
    test(o1, o124, '125', '4')

    res1=str(o19+o124+o1)
    print(str(o19)+'+'+str(o124)+'+'+str(o1)+'='+str(res1), end='  ')
    assert res1=='134'

    res2=str((o19+o124)*o1)
    print('('+str(o19)+'+'+str(o124)+')'+'*'+str(o1)+'='+res2, end='  ')
    assert res2=='3'

    #Check types
    type_o1=type(o1)
    if 'NumericString' in str(type_o1):
        print('Type of NumericString(1) is ok')
    else:
        assert False

    type_o1_plus_o124=type(o1+o124)
    if 'NumericString' in str(type_o1_plus_o124):
        print('Type of NumericString(1)+NumericString(124) is ok')
    else:
        assert False

    type_o1_times_o124=type(o1*o124)
    if 'NumericString' in str(type_o1_times_o124):
        print('Type of NumericString(1)*NumericString(124) is ok')
    else:
        assert False


"""
        ret=callpythoncode(my_code, input='')

        for s in expected_output:
            if not s in ret:
                print(32*'-')
                print('Expected result "'+s+'" not found on output!')
                print(32*'-')
                print('Result="""')
                print(ret)
                print('"""')
            self.assertTrue(s in ret)
            
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

