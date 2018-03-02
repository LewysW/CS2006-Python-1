from twisted_integer import *

class IteratorOfTwistedIntegers:
    def __init__(self, twistedIntegers):
        self.twistedIntegers = twistedIntegers
        self.index = 0

    def hasNext(self):
        return self.index <= self.twistedIntegers.Size()

    def next(self):
        if not(self.hasNext()):
            raise IndexError("Index of iterator is greater than or equal to length of twistedIntegers")

        element = self.twistedIntegers.integers[self.index]
        self.index += 1
        return element
