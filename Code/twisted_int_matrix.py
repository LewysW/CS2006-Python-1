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
            >>> a = TwistedInt(1,3)
            >>> b = TwistedInt(2,3)
            >>> c = TwistedIntMatrix(2, 3, [a, a, a, b, b, b])
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
        for i in range(x):
            self.matrix.append([])
            for j in range(y):
                self.matrix[i].append(self.twistedInts[currentInt])
                currentInt += 1


    def __str__(self):
        """Prints the contents of the matrix.

        Uses the str function of TwistedInt to output the contents of the matrix

        Returns:
            str: returns the output of the matrix as a string

        Examples:
            >>> a = TwistedInt(1,3)
            >>> b = TwistedInt(2,3)
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
        if isinstance(other, TwistedInt):
            result = self.twistedIntMul(other)
            return result
                # raises exceptions
        if not isinstance(other, TwistedIntMatrix):
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
                results.append(self.calcDotProduct(self.matrix[x], other.getCol(y), self.n))
                # returns the result
        return TwistedIntMatrix(self.x, other.y, results)


    def calcDotProduct(self, row, col, n):
        """Calculates the 'Dot Product' of a row & column of two matrices.

        All elements of a row . all elements of a column
        e.g. (1, 2) . (3)
                      (4)
            = (1 * 3) + (2 * 4)
              (but using twistedInt multiplication and addition) 
        This should only be called from __mul__, so shouldn't need to check for / raise exceptions

        Args:
            row - a row of a matrix for the dotProduct
            col - a column of the matrix for the dotProduct
            n - Mod value of the twistedInts in the matrix

        Returns:
            TwistedInt - the value of the dotProduct

        Examples:
            >>> a = TwistedInt(1,2)
            >>> aa = TwistedIntMatrix(2, 2, [a, a, a, a])
            >>> print(aa.calcDotProduct([a, a], [a, a], 2))
            <0:2>
        """
                # initialises return value
        dotProduct = TwistedInt(0, n)
                # dot products
        for i in range(len(row)):
            dotProduct += row[i] * col[i]
        return dotProduct


    def getCol(self, y):
        """Gets all results in a single column of a matrix.

        Iterates through rows of a matrix, adding elements of a single column to a list

        Args:
            y - the y column number to find 

        Returns:
            list - a list of all the values in the column given

        Examples:
            >>> a = TwistedInt(1,2)
            >>> aa = TwistedIntMatrix(2, 2, [a, a, a, a])
            >>> col = aa.getCol(0)
            >>> for t in col:
            ...     print(t)
            <1:2>
            <1:2>
        """
                # initialise return list
        col = []
                # populate list
        for x in range(self.x):
            col.append(self.matrix[x][y])

        return col

    def twistedIntMul(self, tInt):
        """Multiplies a matrix by a TwistedInt.

        This should only be called from __mul__, so no need to check type of tInt or raise exceptions

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
    
    def __add__(self, other):
        if isinstance(other, TwistedInt):
            result = self.twistedIntAdd(other)
            return result
        
        raise Exception("Add function unimplemented")
    
    def twistedIntAdd(self, tInt):
        """Adds TwistedInt to all elements in a matrix.

        This should only be called from __add__, so no need to check type of tInt

        Args:
            tInt - TwistedInt to add

        Returns:
            TwistedIntMatrix - the matrix result of the addition

        Examples:
            >>> a = TwistedInt(2,4)
            >>> aa = TwistedIntMatrix(1, 2, [a, a])
            >>> print(aa + a)
            <0:4> <0:4> 
        """
                # initialises
        results = []
                # performs addition
        for x in range(self.x):
            for y in range(self.y):
                results.append(self.matrix[x][y] + tInt)
        return TwistedIntMatrix(self.x, self.y, results)


def getPossibleMatrices(matrices):
    """Returns all the possible results of multiplying together a list of matrices.

    Args:
        martices - a list of matrices to look at

    Returns:
        list - a list of all the possible matrix results

    Raises:
        IndexError

    Examples:
        >>> a = TwistedInt(1,2)
        >>> aa = TwistedIntMatrix(2, 2, [a, a, a, a])
        >>> list = getPossibleMatrices([aa, aa])
        >>> for m in list:
        ...     print(m)
        <0:2> <0:2>  
        <0:2> <0:2>  
    """
            # raises exceptions
    if len(matrices) == 0:
        raise IndexError("Expected a list containing 1 or more matrices")

    from itertools import permutations
            # list to store results. Set can't tell difference between matrix objects
    results = []
            # iterates over the unique permutations of index orderings
    for x in sorted(set(permutations(range(len(matrices)), len(matrices)))):
            # initialises temp with matrix at 0th index for current permutation
        temp = matrices[x[0]]
        try:
            # iterates over indices of remaining matrices
            for i in range(1, len(x)):
            # multiplies initial matrix by every other index
                temp *= matrices[x[i]]

            # adds result to list
            if not(contains(matrices, temp)):
                results.append(temp)
        except ValueError:
            # if matrices are not computable then contiues to next permutation of matrice orderings
            continue

    return results


def contains(matrixList, matrix):
    """Checks to see if a matrix is present in a list.

    Args:
        matrixList - a list of matrices
        matrix - the matrix to look for in the list

    Returns:
        bool - True if inside the list, False if not

    Raises:
        TypeError
        IndexError

    Examples:
        >>> a = TwistedInt(1,2)
        >>> aa = TwistedIntMatrix(1,1,[a])
        >>> bb = TwistedIntMatrix(1,2,[a,a])
        >>> list = [aa, aa]
        >>> contains(list, bb)
        False
        >>> contains(list, aa)
        True
    """
            # raises exceptions
    if type(matrixList) is not list:
        raise TypeError("Expected first argument to be a list of TwistedIntMatrix")
    if not isinstance(matrix, TwistedIntMatrix):
        raise TypeError("Expected second argument to be a TwistedIntMatrix")
    if matrixList == []:
        raise IndexError("Expected a list containing 1 or more Matrices")
            # iterate through list
    for m in matrixList:
        if equalMatrices(m, matrix):
            return True
    return False

def equalMatrices(m1, m2):
    """Returns true or false if matrices are the same

    Args:
        m1 - a matrix
        m2 - a matrix

    Returns:
        bool - True if same, False otherwise

    Examples:
        >>> a = TwistedInt(2,4)
        >>> aa = TwistedIntMatrix(1, 2, [a, a])
        >>> bb = TwistedIntMatrix(1, 2, [a, a])
        >>> cc = TwistedIntMatrix(2, 1, [a, a])
        >>> equalMatrices(aa, aa)
        True
        >>> equalMatrices(aa, bb)
        True
        >>> equalMatrices(aa, cc)
        False
    """
            # check same size
    if m1.x != m2.x or m1.y != m2.y:
        return False
            # initialise iterators
    i1 = IteratorOfTwistedIntMatrix(m1)
    i2 = IteratorOfTwistedIntMatrix(m2)
            # go through iterators and check that next() is the same
    while i1.hasNext() and i2.hasNext():
        if i1.next().object != i2.next().object:
            return False
    return True

class IteratorOfTwistedIntMatrix:
    """Iterator for a Matrix of TwistedInts
    """

    def __init__(self, matrix):
        """Creates a new Iterator.

        Iterator is linked to a Matrix of TwistedInts, and is used for iterating through the matrix

        Args:
            matrix - TwistedIntMatrix to be iterated through

        Creates:
            IteratorOfTwistedIntMatrix - the iterator to iterate through a matrix

        Raises:
            TypeError

        Examples:
            >>> a = TwistedInt(1,2)
            >>> aa = TwistedIntMatrix(1,1,[a])
            >>> iterator = IteratorOfTwistedIntMatrix(aa)
            >>> iterator.hasNext()
            True
        """
                # raises exceptions
        if not isinstance(matrix, TwistedIntMatrix):
            raise TypeError("Expected arument to be a TwistedIntMatrix")
                # initialises
        self.twistedIntMatrix = matrix
        self.x = 0
        self.y = 0


    def hasNext(self):
        """Checks to see if there is another element in the iterator
        
        Returns:
            bool - True if iterator has next, False otherwise

        Examples:
            >>> a = TwistedInt(1,2)
            >>> aa = TwistedIntMatrix(1,1,[a])
            >>> iterator = IteratorOfTwistedIntMatrix(aa)
            >>> iterator.hasNext()
            True
        """

        return (self.x < self.twistedIntMatrix.x) and (self.y < self.twistedIntMatrix.y)

    def next(self):
        """Gets the next element of the Matrix.

        Goes through the matrix row by row.

        Returns:
            TwistedInt - the next element of the Matrix

        Raises:
            IndexError

        Examples:
            >>> a = TwistedInt(1,2)
            >>> aa = TwistedIntMatrix(1,1,[a])
            >>> iterator = IteratorOfTwistedIntMatrix(aa)
            >>> print(iterator.next())
            <1:2>
        """
                # raises exceptions
        if not(self.hasNext()):
            raise IndexError("Index of iterator is greater than or equal to length of twistedIntegers")
                # initialises element
        element = self.twistedIntMatrix.matrix[self.x][self.y]
        self.y += 1
                # increments iterator
        if (self.y == len(self.twistedIntMatrix.matrix[self.x])):
            self.x += 1
            self.y = 0

        return element


"""Run Doctest in Docstrings"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()