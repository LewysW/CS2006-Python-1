from twisted_integers import *

class TwistedIntMatrix:

    # Creates a twisted int matrix of dimensions x, y with list of int values
    # default values of ints are 0
    def __init__(self, x, y, ints):
        self.x = x
        self.y = y
        self.matrix = []
        self.twistedInts = ints

        # Raises an IndexError if number of elements in matrix and list are unequal
        if not(x * y == len(self.twistedInts)):
            raise IndexError("Number of elements in matrix and list do not match.")

        self.n = self.twistedInts[0].n

        # Raises MismatchedModException if a value in the matrix has a different n to the rest.
        for twistedInt in self.twistedInts:
            if not(twistedInt.n == n):
                raise MismatchedModException("Twisted ints do not all have the same mod value.")

        # Populates the matrix using the list of twisted ints.
        currentInt = 0
        for i in range(0, x):
            self.matrix.append([])
            for j in range(0, y):
                self.matrix[i].append(self.twistedInts[currentInt])
                currentInt += 1

        self.iterator = IteratorOfTwistedIntMatrix(self)

    # Prints all values in the twisted int matrix
    def __str__(self):
        out = ""

        while self.iterator.hasNext():
            out += str(self.iterator.next()) + "\n"

        return out

    # define "*"
    def __mul__(self, other):


    # define "+"
    def __add__(self, other):
        

class IteratorOfTwistedIntMatrix:
    # Sets twistedIntegers to list to be iterated over
    # and sets initial index to 0
    def __init__(self, matrix):
        self.twistedIntMatrix = matrix
        self.x = 0
        self.y = 0

    # Checks if iterator has next element from TwistedIntegers
    def hasNext(self):
        return (self.x < self.twistedIntMatrix.x) and (self.y < self.twistedIntMatrix.y)

    # Gets next element from TwistedIntegers if there is one and increments Index
    # otherwise raises index error.
    def next(self):
        if not(self.hasNext()):
            raise IndexError("Index of iterator is greater than or equal to length of twistedIntegers")

        element = self.twistedIntMatrix.matrix[self.x][self.y]
        self.y += 1

        if (self.y == len(self.twistedIntMatrix.matrix[self.x])):
            self.x += 1
            self.y = 0

        return element
