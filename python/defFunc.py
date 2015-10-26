#!c:/Python34/python.exe -u
# -*- coding: utf-8 -*-

import sys

aNumber = int(sys.argv[1])

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
    print()
		
def fib2(n): # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

print("...fib(n)...")
print(fib(aNumber))
print("...fib2(n)...")
print(fib2(aNumber))
