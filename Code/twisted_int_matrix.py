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
            if not(twistedInt.n == self.n):
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

        # Current number of ints in matrix added to output
        currentInt = 0

        while self.iterator.hasNext():
            out += str(self.iterator.next()) + " "

            currentInt += 1

            # Decides whether to print a new line based on y dimension and current int
            if (currentInt % self.y) == 0:
                out += "\n"

        self.iterator = IteratorOfTwistedIntMatrix(self)
        return out

    # define "*"
    def __mul__(self, other):
        if not(self.y == other.x):
            raise ValueError("Y dimension of matrix a is not equal to X dimension of matrix b.")

        if not(self.n == other.n):
            raise MismatchedModException("Mod value of matrix a is not equal to mod value of matrix b.")

        results = []

        for x in range(0, self.x):
            for y in range(0, other.y):
                results.append(self.calcDotProduct(self.matrix[x], self.getCol(other, y), self.n))

        return TwistedIntMatrix(self.x, other.y, results)

    # Gets the dot product of a given row and column of two matrices
    def calcDotProduct(self, list1, list2, n):
        dotProduct = TwistedInt(0, n)

        for i in range(0, len(list1)):
            dotProduct += list1[i] * list2[i]

        return dotProduct

    # Returns the column at index y of a given matrix
    def getCol(self, intMatrix, y):
        col = []
        for x in range(0, intMatrix.x):
            col.append(intMatrix.matrix[x][y])

        return col

    # define "+"
    #def __add__(self, other):

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
