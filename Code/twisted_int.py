from exceptions import *

class TwistedInt:
    """A special type of Integer, but with special rules.
    
    Acts like a normal Int, but also has special functions
    for addition and multiplication (as well as converting to a string)
    """

    # TODO Add unit tests for current functions
    def __init__(self, val, n):
        """Creates a new TwistedInt object.
        
        A TwistedInt has two values assigned to it, a main value and the mod value.
        An exception is thrown if args are incorrect.
        
        Args
            val - value of the TwistedInt
            n - mod value of the TwistedInt
        
        Creates:
            TwistedInt - a new type of Int

        Raises:
            TypeError
            InvalidModError
            InvalidValError

        Examples:
            >>> a = TwistedInt(2, 3)
        """
                # raises exceptions
        if type(val) is str:
            raise TypeError("TwistedInt() argument #1 (Value) must be an int")
        if type(n) is str:
            raise TypeError("TwistedInt() argument #2 (Mod) must be an int")
        if n < 0:
            raise InvalidModError("TwistedInt() argument #2 (Mod) must be greater than 0")
        if val < 0 or val >= n:
            raise InvalidValError("TwistedInt() argument #1 (Value) must be in the domain {0,1,..,n-1}")
                # initialises
        self.object = int(val)
        self.n = int(n)


    def __str__(self):
        """Outputs the value of the TwistedInt as a string.

        The TwistedInt is formatted between two spikey bois <>.
        The Value of the TwistedInt is followed by the Mod value of the TwistedInt.

        Returns:
            str: the value and mod of the TwistedInt, in the form <val:mod>
        
        Examples:
            >>> str(TwistedInt(1,2))
            '<1:2>'
            >>> a = TwistedInt(2, 3)
            >>> print(a)
            <2:3>
        """
                # outputs as <val:mod>
        return "<" + str(self.object)+ ":" + str(self.n) + ">"


    def __mul__(self, other):
        """Redefines multiplication rules for TwistedInts, following the rule: a * b = (a + b + a . b) mod n.

        Args:
            self - this TwistedInt
            other - the TwistedInt to multiply by

        Returns:
            TwistedInt - result of multiplication of two TwistedInts

        Raises:
            MismatchedModError

        Examples:
            >>> a = TwistedInt(1,5)
            >>> b = TwistedInt(2,5)
            >>> print(a * b)
            <0:5>
            >>> a = TwistedInt(1,7)
            >>> b = TwistedInt(2,7)
            >>> print(a * b)
            <5:7>
        """
                # raises exceptions
        if self.n != other.n:
            raise MismatchedModError("Cannot multiply together two TwistedInts with different Mod values")
                # returns result of multiplication
        mulValue = self.object + other.object + self.object * other.object
        return TwistedInt(mulValue % self.n, self.n)


    def __add__(self, other):
        """Redefines addition rules for TwistedInts, following the rule: a + b = (a + b) mod n.

        Args:
            self - this TwistedInt
            other - the TwistedInt to add to

        Returns:
            TwistedInt - the result of addition of two TwistedInts

        Raises:
            MismatchedModError

        Examples:
            >>> a = TwistedInt(1,4)
            >>> b = TwistedInt(2,4)
            >>> print(a + b)
            <3:4>
            >>> a = TwistedInt(2,4)
            >>> b = TwistedInt(3,4)
            >>> print(a + b)
            <1:4>
        """
                # raises exceptions
        if self.n != other.n:
            raise MismatchedModError("Cannot add together two TwistedInts with different Mod values")
                # returns result of addition
        addValue = self.object + other.object
        return TwistedInt(addValue % self.n, self.n)        


"""Run Doctest in Docstrings"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()