from twisted_int import *

class TwistedIntegers:
    """A list of all TwistedInts inside inside the set of numbers Zn."""

    def __init__(self, n):
        """Creates a new TwistedIntegers object.
        
        For every value in Zn (every value under n), a new TwistedInt is created and added to the list.
        
        Args:
            n - mod value of the TwistedInt
                also the range for Zn
        
        Creates:
            TwistedIntegers - a list of TwistedIntegers
        
        Raises:
            TypeError
            InvalidModError

        Examples:
            >>> print(TwistedIntegers(5))
            <0:5>
            <1:5>
            <2:5>
            <3:5>
            <4:5>
        """
                # raises exceptions
        if type(n) is str:
            raise TypeError("TwistedInt() argument must be an int")
        if n < 0:
            raise InvalidModError("TwistedInt() argument must be greater than 0")

        self.integers = []
        self.n = n
                # populates list
        for i in range(n):
            self.integers.append(TwistedInt(i, n))


    def __str__(self):
        """Prints the contents of the list.

        Uses an iterator to iterate through the list of TwistedIntegers,
        printing them out using the TwistedInt str function.
        
        Returns:
            str - the contents of the list

        Examples:
            >>> print(TwistedIntegers(5))
            <0:5>
            <1:5>
            <2:5>
            <3:5>
            <4:5>
        """
                # initialises the string
        out = ""
        self.iterator = IteratorOfTwistedIntegers(self)
                # uses the iterator to output all values
        while self.iterator.hasNext():
            out += str(self.iterator.next()) + "\n"
            
        return out[:-1] # removes new line character


    def size(self):
        """Returns the size of the list.

        Returns:
            int - size of the list

        Examples:
            >>> a = TwistedIntegers(5)
            >>> a.size()
            5
        """

        return self.n


class IteratorOfTwistedIntegers:
    """Iterator for TwistedIntegers"""
    def __init__(self, twistedIntegers):
        """Creates a new Iterator
        
        Args:
            TwistedIntegers - twistedIntegers
        
        Creates:
            IteratorOfTwistedIntegers - an iterator to iterate over TwistedIntegers 

        Raises:
            TypeError
        
        Examples:
            >>> i = IteratorOfTwistedIntegers(TwistedIntegers(5))
        """
                # raises exceptions
        if type(twistedIntegers) is not TwistedIntegers:
            raise TypeError("IteratorOfTwistedIntegers() argument is not a TwistedIntegers object")
                # initialises
        self.twistedIntegers = twistedIntegers
        self.index = 0


    def hasNext(self):
        """Checks if iterator has next element from TwistedIntegers.
        
        Returns:
            bool - True if there is a next element in the list, False if not
        
        Examples:
            >>> i = IteratorOfTwistedIntegers(TwistedIntegers(5))
            >>> i.hasNext()
            True            
        """

        return self.index < self.twistedIntegers.size()


    def next(self):
        """Gets next element from TwistedIntegers if there is one and increments Index.

        Returns:
            TwistedInt - next element in the list

        Raises:
            IndexError

        Examples:
            >>> i = IteratorOfTwistedIntegers(TwistedIntegers(5))
            >>> print(i.next())
            <0:5>
            >>> print(i.next())
            <1:5>
        """
                # raises exceptions
        if not(self.hasNext()):
            raise IndexError("Index of iterator is greater than or equal to length of twistedIntegers")
                # finds and returns next element from list
        element = self.twistedIntegers.integers[self.index]
        self.index += 1
        return element


def findValAdd(n):
    """Finds all values in the range Zn where t + x = x

    Uses iterator to find all values to test against, then tests them to see
    if valid, add them to the list.

    Args:
        n - range for Zn

    Returns:
        list - of TwistedIntegers

    Raises:
        InvalidModError

    Examples:
        >>> findValAdd(3)
        ['<0:3>']
    """

    if n < 0:
        raise InvalidModError("argument must be greater than 0")

    iteratorT = iteratorX = IteratorOfTwistedIntegers(TwistedIntegers(n))
    validIntegers = []
    validInt = True

    while iteratorT.hasNext():
        t = iteratorT.next()
        iteratorX = IteratorOfTwistedIntegers(TwistedIntegers(n))

        while iteratorX.hasNext():
            x = iteratorX.next()

            if (t + x).object != x.object:
                validInt = False
                break

        if validInt:
            validIntegers.append(str(t))

        validInt = True

    return validIntegers


def findValMul(n):
    """Finds all values in the range Zn where e + x = x

    Uses iterator to find all values to test against, then tests them to see
    if valid, add them to the list.

    Args:
        n - range for Zn

    Returns:
        list - of TwistedIntegers

    Raises:
        InvalidModError

    Examples:
        >>> findValMul(3)
        ['<0:3>']
    """

    if n < 0:
        raise InvalidModError("argument must be greater than 0")

    iteratorE = iteratorX = IteratorOfTwistedIntegers(TwistedIntegers(n))
    validIntegers = []
    validInt = True

    while iteratorE.hasNext():
        e = iteratorE.next()
        iteratorX = IteratorOfTwistedIntegers(TwistedIntegers(n))

        while iteratorX.hasNext():
            x = iteratorX.next()

            if (e + x).object != x.object:
                validInt = False
                break

        if validInt:
            validIntegers.append(str(e))

        validInt = True

    return validIntegers


"""Run Doctest in Docstrings"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()