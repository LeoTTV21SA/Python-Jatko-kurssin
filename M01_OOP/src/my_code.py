

import sys
import time

class NumericString:
       #Implement class here!
    def __init__(self, value):
        if value < 0:
            raise ValueError("Negative values are not allowed")
        self.value = str(value)
    
    def __str__(self):
        return self.value
    
    def __add__(self, other):
        if not isinstance(other, NumericString):
            raise TypeError("Can only add NumericString to NumericString")
        # Tasaa numerot etunollien kanssa
        num1 = list(self.value.zfill(max(len(self.value), len(other.value))))
        num2 = list(other.value.zfill(max(len(self.value), len(other.value))))
        
        # Lisää numero numerolta modulo 10:llä
        result = ''
        for d1, d2 in zip(num1, num2):
            result += str((int(d1) + int(d2)) % 10)
            
        # Poista etunollat
        result = result.lstrip('0') or '0'
        return NumericString(int(result))
    
    def __mul__(self, other):
        if not isinstance(other, NumericString):
            raise TypeError("Can only multiply NumericString with NumericString")
        # Tasaa numerot etunollien kanssa
        num1 = list(self.value.zfill(max(len(self.value), len(other.value))))
        num2 = list(other.value.zfill(max(len(self.value), len(other.value))))
        
        # Numeroittainen kertolasku modulo 10:llä
        result = ''
        for d1, d2 in zip(num1, num2):
            result += str((int(d1) * int(d2)) % 10)
            
        # Poista etunollat
        result = result.lstrip('0') or '0'
        return NumericString(int(result))
 # Sample test program you can use to test your implementation
if __name__ == "__main__":
    #Luo testiobjekteja ja testausarvoraja
    o16 = NumericString(16)
    try:
        print('Initializing with negative integer...', end=' ')
        o_exception = NumericString(-1)
        got_exception = False
    except:
        got_exception = True

    assert got_exception
    print('Got exception -- ok')
    
    o124 = NumericString(124)
    o19 = NumericString(19)
    o0 = NumericString(0)
    o1 = NumericString(1)

    def test(o1, o2, expected_value1, expected_value2):
        res1 = o1 + o2
        print(f'"{str(o1)}+{str(o2)}={str(res1)}"', end='  ')
        assert str(res1) == expected_value1
        print('ok')
        res2 = o1 * o2
        print(f'"{str(o1)}*{str(o2)}={str(res2)}"', end='  ')
        assert str(res2) == expected_value2
        print('ok')
        
    # Test cases
    test(o124, o19, '133', '26')
    test(o124, o0, '124', '0')
    test(o124, o1, '125', '4')

    test(o19, o124, '133', '26')
    test(o0, o124, '124', '0')
    test(o1, o124, '125', '4')

    res1 = o19 + o124 + o1
    print(f'"{str(o19)}+{str(o124)}+{str(o1)}={str(res1)}"', end='  ')
    assert str(res1) == '134'
    print('ok')

    res2 = (o19 + o124) * o1
    print(f'"({str(o19)}+{str(o124)})*{str(o1)}={str(res2)}"', end='  ')
    assert str(res2) == '3'
    print('ok')

    # Type checking
    type_o1 = type(o1)
    if 'NumericString' in str(type_o1):
        print('Type of NumericString(1) is ok')
    else:
        assert False

    type_o1_plus_o124 = type(o1 + o124)
    if 'NumericString' in str(type_o1_plus_o124):
        print('Type of NumericString(1)+NumericString(124) is ok')
    else:
        assert False

    type_o1_times_o124 = type(o1 * o124)
    if 'NumericString' in str(type_o1_times_o124):
        print('Type of NumericString(1)*NumericString(124) is ok')
    else:
        assert False