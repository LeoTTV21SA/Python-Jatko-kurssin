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
            'Initial value of Point.getter_count()==0',
            'Point(-1, 2) created',
            'Point(3, 4) created',
            'Point(-3, -4) created',
            'Point(0.122, 0.2112) created',
            'Point(0.111, -277272.272) created',
            'Test Point(0.111, -277272.272)',
            'Point(0.111, -277272.272): Accessing x increases Point.getter_count()',
            'Point(0.111, -277272.272): Accessing y increases Point.getter_count()',
            'Point(0.111, -277272.272): Writing x and y values seems to work',
            'Point(0.111, -277272.272): Point.getter_count() not increasing when not read x or y.',
            'Test Point(0.111, -277272.272) completed',
            'Test Point(0.111, -277272.272)',
            'Point(0.111, -277272.272): Accessing x increases Point.getter_count()',
            'Point(0.111, -277272.272): Accessing y increases Point.getter_count()',
            'Point(0.111, -277272.272): Writing x and y values seems to work',
            'Point(0.111, -277272.272): Point.getter_count() not increasing when not read x or y.',
            'Test Point(0.111, -277272.272) completed',
            'Test Point(0.111, -277272.272)',
            'Point(0.111, -277272.272): Accessing x increases Point.getter_count()',
            'Point(0.111, -277272.272): Accessing y increases Point.getter_count()',
            'Point(0.111, -277272.272): Writing x and y values seems to work',
            'Point(0.111, -277272.272): Point.getter_count() not increasing when not read x or y.',
            'Test Point(0.111, -277272.272) completed',
            'Test Point(0.111, -277272.272)',
            'Point(0.111, -277272.272): Accessing x increases Point.getter_count()',
            'Point(0.111, -277272.272): Accessing y increases Point.getter_count()',
            'Point(0.111, -277272.272): Writing x and y values seems to work',
            'Point(0.111, -277272.272): Point.getter_count() not increasing when not read x or y.',
            'Test Point(0.111, -277272.272) completed',
            'Test Point(0.111, -277272.272)',
            'Point(0.111, -277272.272): Accessing x increases Point.getter_count()',
            'Point(0.111, -277272.272): Accessing y increases Point.getter_count()',
            'Point(0.111, -277272.272): Writing x and y values seems to work',
            'Point(0.111, -277272.272): Point.getter_count() not increasing when not read x or y.',
            'Test Point(0.111, -277272.272) completed'
        ]
        
        my_code="""
import sys
sys.path.insert(0, '../src')

from my_code import Point


if True:
    assert Point.getter_count()==0
    print('Initial value of Point.getter_count()==0')

    points=[]
    coords=[(-1, 2), (3,4), (-3, -4), (0.122, 0.2112), (0.111, -277272.272)]
    for coord in coords:
        points.append(Point(coord[0], coord[1]))
        print('Point('+str(coord[0])+', '+str(coord[1])+') created')

    earlier_getter_count=Point.getter_count()

    for p, c in zip(points, coords):
        print(32*'-')
        pstr='Point('+str(coord[0])+', '+str(coord[1])+')'
        print('Test '+pstr)
        a=p.x
        assert Point.getter_count()>=(earlier_getter_count+1)
        print(pstr+': Accessing x increases Point.getter_count()')
        b=p.y
        assert Point.getter_count()>=(earlier_getter_count+2)
        print(pstr+': Accessing y increases Point.getter_count()')

        p.x=-p.x
        p.y=-p.y
        assert Point.getter_count()>=(earlier_getter_count+4)
        
        assert p.x==(-c[0])
        assert p.y==(-c[1])
        print(pstr+': Writing x and y values seems to work')
        
        earlier_getter_count=Point.getter_count()

        for _ in range(10):
            assert earlier_getter_count==Point.getter_count()

        print(pstr+': Point.getter_count() not increasing when not read x or y.')

        print('Test Point('+str(coord[0])+', '+str(coord[1])+') completed')

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

