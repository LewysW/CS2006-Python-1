"""Implement new class called TwistedIntegers which will represent Zn with respect to the operations 
    a⊕b = (a+b) mod n
    a⊗b = (a+b+a· b) mod n.
It should have at least three methods: __init__, __str__ and Size, where Size should return the number of elements in Zn."""

from twisted_int import *

class TwistedIntegers:

        def __init__(self, n):
            while (type(n) is str):
                    n = int(input("Please re-enter your n (mod) value (must be greater than or equal to 0):\n"))
            self.integers = []
            self.n = n
            for i in range(n):
                self.integers.append(TwistedInt(i, n))
            
        def __str__(self):
            return "<_:" + str(self.n) + ">"

        def size(self):
            return self.n - 1



