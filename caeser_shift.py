import collections
import string
#
#
# def caeser_shift(s,k):
#     s = s.lower()
#     alphabet = collections.deque(string.ascii_lowercase)
#     alphabet.rotate(k)
#     str_arr = ''.join(list(alphabet))
#     trans = str.maketrans(str_arr,string.ascii_lowercase )
#     return s.translate(trans)
# print(caeser_shift('abc.-79', 2))




def caeser_shift_math(s,k):
    s = s.lower()
    shifted_arr = []
    alphabet = collections.deque(string.ascii_lowercase)
    for i in s:
        if i in alphabet:
            shifted_arr.append(chr(((ord(i) - 97 + k) % 26 ) + 97))
        else:
            shifted_arr.append(i)
    return ''.join(shifted_arr)
print(caeser_shift_math('a b c 54556', 4))

