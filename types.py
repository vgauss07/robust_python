"""
Types convey info about
behaviors and constraints
to the Python language.

communicates same to other
developers
"""

from ctypes import string_at
from sys import getsizeof
from binascii import hexlify

a = 0b01010000_01000001_01010100
print(a)

# prints out memory of the variable
print(hexlify(string_at(id(a), getsizeof(a))))

text = "PAT"
print(hexlify(string_at(id(text), getsizeof(text))))