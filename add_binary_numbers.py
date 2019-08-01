'''
Add two binary numbers

input to function = 2 strings (binary numbers)
make sure string are of equal length
define rules for addition
0,0 = 0
0,1 = 1
1,0 = 1
1,1 = 0, carry 1
take care of carry forward operation

'''

import unittest

def add_binary_number(a,b):
    if not a or not b:
        return ''
    if len(a) < len(b):
        a = 0 * (len(b) - len(a)) + a
    elif len(b) < len(a):
        b = 0 * (len(a) - len(b)) + b
    i = len(a) - 1
    c = ''
    carry = 0
    while i >= 0:
        sum = int(a[i]) + int(b[i])
        if sum == 2:
            if carry == 0:
                carry = 1
                c += '0'
            else:
                c += '1'
        elif sum == 1:
            if carry == 1:
                c += '0'
            else:
                c += '1'
        else:
            if carry == 1:
                c += '1'
                carry = 0
            else:
                c += '0'
        i -= 1
    return c[::-1]


class Test(unittest.TestCase):
    def test1(self):
        a = '0001'
        b = '0010'
        c = add_binary_number(a,b)
        expected = '0011'
        self.assertEqual(c,expected)


unittest.main()