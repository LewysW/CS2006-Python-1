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
            # Declares iterator for TwistedIntegers instance
            self.iterator = IteratorOfTwistedIntegers(self)

        # Prints out TwistedIntegers using iterator
        def __str__(self):
            out = ""
            # Iterates over TwistedIntegers while there is another elements
            # and appends each to a string to be returned
            while self.iterator.hasNext():
                out += str(self.iterator.next()) + "\n"
            return out

        def size(self):
            return self.n

# Iterator for TwistedIntegers
class IteratorOfTwistedIntegers:
    # Sets twistedIntegers to list to be iterated over
    # and sets initial index to 0
    def __init__(self, twistedIntegers):
        self.twistedIntegers = twistedIntegers
        self.index = 0

    # Checks if iterator has next element from TwistedIntegers
    def hasNext(self):
        return self.index < self.twistedIntegers.size()

    # Gets next element from TwistedIntegers if there is one and increments Index
    # otherwise raises index error.
    def next(self):
        if not(self.hasNext()):
            raise IndexError("Index of iterator is greater than or equal to length of twistedIntegers")

        element = self.twistedIntegers.integers[self.index]
        self.index += 1
        return element

def tauPlusXEqualsX(n):
    """Finds valid values of τ where τ ⊕ x = x"""
    iteratorT = iteratorX = IteratorOfTwistedIntegers(TwistedIntegers(n))
    validIntegers = []
    validInt = True

    while iteratorT.hasNext():
        τ = iteratorT.next()
        iteratorX = IteratorOfTwistedIntegers(TwistedIntegers(n))

        while iteratorX.hasNext():
            x = iteratorX.next()

            if (τ + x).object != x.object:
                validInt = False
                break

        if validInt:
            validIntegers.append(str(τ))

        validInt = True

    return validIntegers

def epsilonMulXEqualsX(n):
    """Finds valid values of ε where ε ⊗ x = x"""
    iteratorE = iteratorX = IteratorOfTwistedIntegers(TwistedIntegers(n))
    validIntegers = []
    validInt = True

    while iteratorE.hasNext():
        ε = iteratorE.next()
        iteratorX = IteratorOfTwistedIntegers(TwistedIntegers(n))

        while iteratorX.hasNext():
            x = iteratorX.next()

            if (ε + x).object != x.object:
                validInt = False
                break

        if validInt:
            validIntegers.append(str(ε))

        validInt = True

    return validIntegers


