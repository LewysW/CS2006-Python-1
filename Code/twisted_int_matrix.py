from twisted_integers import *

class TwistedIntMatrix:
    """A Matrix of TwistedInts.

    Stores a matrix of TwistedInts as a list. These can then be added to or multiplied with other matrices.
    """

    def __init__(self, x, y, tInts):
        """Creates a matrix, populated with TwistedInts

        Args:
            x - x size of the matrix
            y - y size of the matrix
            tInts - a list of TwistedInt objects

        Creates:
            TwistedIntMatrix - a collections of TwistedInts
            
        Raises:
            MatrixIndexError
            MismatchedModError

        Examples:
            >>> a = TwistedInt(1,3); b = TwistedInt(2,3)
            >>> print(TwistedIntMatrix(2, 3, [a, a, a, b, b, b]))
            <1:3> <1:3> <1:3>
            <2:3> <2:3> <2:3>
        """
                # raises exceptions
        if x < 0 or y < 0:
            raise MatrixIndexError("Size of matrix must be larger than 0")
        if x * y != len(tInts):
            raise MatrixIndexError("Number of elements in matrix and list do not match.")
        for twistedInt in tInts:
            if twistedInt.n != tInts[0].n:
                raise MismatchedModError("Twisted ints do not all have the same mod value.")
                # initialise
        self.x = x
        self.y = y
        self.matrix = []
        self.twistedInts = tInts
        self.n = tInts[0].n
        self.iterator = IteratorOfTwistedIntMatrix(self)
                # populates the matrix using the list of twisted ints.
        currentInt = 0
        for i in range(0, x):
            self.matrix.append([])
            for j in range(0, y):
                self.matrix[i].append(self.twistedInts[currentInt])
                currentInt += 1


    def __str__(self):
        """Prints the contents of the matrix.

        Uses the str function of TwistedInt to output the contents of the matrix

        Returns:
            str: returns the output of the matrix as a string

        Examples:
            >>> a = TwistedInt(1,3); b = TwistedInt(2,3)
            >>> print(TwistedIntMatrix(2, 3, [a, a, a, b, b, b]))
            <1:3> <1:3> <1:3>
            <2:3> <2:3> <2:3>
        """
                # initialises the string
        out = ""
        self.iterator = IteratorOfTwistedIntMatrix(self)
                # current number of ints in matrix added to output
        currentInt = 0
                # use iterator to output all values
        while self.iterator.hasNext():
            out += str(self.iterator.next()) + " "
            currentInt += 1
                # adds a new line character if needed
            if (currentInt % self.y) == 0:
                out += "\n"
        return out[:-1] # removes new line


    def __mul__(self, other):
        """Multiplies a matrix by another matrix.

        Multiplies the matrix using proper 'dot-product' multiplication methods

        Args:
            other - the other matrix to multiply this matrix by
                or a TwistedInt to multiply the matrix by

        Returns:
            TwistedIntMatrix - the result of the matrix multiplication

        Raises:
            ValueError
            MismatchedModError

        Examples:
            >>> a = TwistedInt(1,3)
            >>> b = TwistedInt(2,3)
            >>> aa = TwistedIntMatrix(2, 2, [a, a, a, a])
            >>> bb = TwistedIntMatrix(2, 2, [a, b, a, b])
            >>> print(aa * bb)
            <0:3> <1:3>
            <0:3> <1:3>

            >>> a = TwistedInt(2,5)
            >>> aa = TwistedIntMatrix(2, 2, [a, a, a, a])
            >>> print(aa * a)
            <3:5> <3:5>
            <3:5> <3:5>
        """
                # switches to multiplying by TwistedInt function
        if type(other) is TwistedInt:
            result = self.twistedIntMul(other)
            return result
                # raises exceptions
        if type(other) is not TwistedIntMatrix:
            raise TypeError("Expected argument to be of type TwistedIntMatrix or TwistedInt")
        if self.y != other.x:
            raise ValueError("Y dimension of matrix a is not equal to X dimension of matrix b")
        if self.n != other.n:
            raise MismatchedModError("Mod value of matrix a is not equal to mod value of matrix b")
                # initialises results
        results = []
                # goes through matrix and does multiplication
        for x in range(self.x):
            for y in range(other.y):
                results.append(self.calcDotProduct(self.matrix[x], self.getCol(other, y), self.n))
                # returns the result
        return TwistedIntMatrix(self.x, other.y, results)

    # Gets the dot product of a given row and column of two matrices
    def calcDotProduct(self, list1, list2, n):
        """
        """
        dotProduct = TwistedInt(0, n)

        for i in range(0, len(list1)):
            dotProduct += list1[i] * list2[i]

        return dotProduct

    # Returns the column at index y of a given matrix
    def getCol(self, intMatrix, y):
        """
        """
        col = []
        for x in range(0, intMatrix.x):
            col.append(intMatrix.matrix[x][y])

        return col

    # TODO cleanup THIS using itertools
    def twistedIntMul(self, tInt):
        """Multiplies a matrix by a TwistedInt.

        This should only be called from __mul__, so no need to check type of tInt

        Args:
            tInt - TwistedInt to multiply by

        Returns:
            TwistedIntMatrix - the matrix result of the multiplication

        Examples:
            >>> a = TwistedInt(2,5)
            >>> aa = TwistedIntMatrix(2, 2, [a, a, a, a])
            >>> print(aa * a)
            <3:5> <3:5>
            <3:5> <3:5>
        """
                # initialises
        results = []
                # performs multiplication
        for x in range(self.x):
            for y in range(self.y):
                results.append(self.matrix[x][y] * tInt)
        return TwistedIntMatrix(self.x, self.y, results)
    
    #TODO also this
    def __add__(self, other):
        return self
    
    #TODO cleanup with itertools same as mul
    def twistedIntAdd(self, tInt):
        """Adds TwistedInt to all elements in a matrix.

        This should only be called from __add__, so no need to check type of tInt

        Args:
            tInt - TwistedInt to add

        Returns:
            TwistedIntMatrix - the matrix result of the addition

        Examples:
        """
                # initialises
        results = []
                # performs addition
        for x in range(self.x):
            for y in range(self.y):
                results.append(self.matrix[x][y] + tInt)
        return TwistedIntMatrix(self.x, self.y, results)

    # Returns the set of possible matrices given a list of matrices
    @staticmethod
    def getPossibleMatrices(matrices):
        from itertools import permutations
        #List to store results. Set can't tell difference between matrix objects
        results = []

        # Iterates over the unique permutations of index orderings
        for x in sorted(set(permutations(range(0, len(matrices)), len(matrices)))):
            # Initialises temp with matrix at 0th index for current permutation
            temp = matrices[x[0]]
            try:
                # Iterates over indices of remaining matrices
                for i in range(1, len(x)):
                    # Multiplies initial matrix by every other index
                    temp *= matrices[x[i]]

                # Adds result to list
                if not(TwistedIntMatrix.contains(results, temp)):
                    results.append(temp)
            except ValueError:
                # If matrices are not computable then contiues to next permutation of matrice orderings
                continue

        return results

    # Returns whether or not matrix is present in list
    @staticmethod
    def contains(matrixList, matrix):
        for i in range(0, len(matrixList)):
            iteratorList = IteratorOfTwistedIntMatrix(matrixList[i])
            iteratorMatrix = IteratorOfTwistedIntMatrix(matrix)

            while (iteratorMatrix.hasNext() and iteratorList.hasNext()):
                equal = (iteratorMatrix.next().object == iteratorList.next().object)

            if (equal):
                return equal

        return False


    # TODO remove this
    @staticmethod
    def test():
        a = TwistedInt(0,9)
        b = TwistedInt(1,9)
        c = TwistedInt(2,9)


        matrix = TwistedIntMatrix(1,1,[a])
        matrix1 = TwistedIntMatrix(1,1,[b])
        matrix2 = TwistedIntMatrix(1,1,[c])

        matrices = [matrix, matrix1,matrix2]

        results = (TwistedIntMatrix.getPossibleMatrices(matrices))

        for x in results:
            print(x)

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
