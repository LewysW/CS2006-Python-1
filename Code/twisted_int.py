from exceptions import *

class TwistedInt:
    """A class of TwistedInt, defined in the specification.
    
    Has special functions for addition and multiplication (as well as converting to a string)"""

    # TODO Add unit tests for current functions
    # TODO move validation code to main
    # Validates user input.
    #Throws and exception for each different invalid piece of user input.
    def __init__(self, obj, n):
        while True:
            try:
                if type(n) is str or n < 0:
                    raise InvalidModException
                elif type(obj) is str or obj < 0 or obj >= n:
                    raise InvalidObjException
                else:
                    self.object = int(obj)
                    self.n = int(n)
                    break
            except InvalidModException:
                n = int(input("Please re-enter your n (mod) value (must be greater than or equal to 0):\n"))
            except InvalidObjException:
                obj = int(input("Please re-enter your integer value (must be in domain 0,1,...,n-1):\n"))


    # overwrite "print"
    def __str__(self):
        return "<" + str(self.object)+ ":" + str(self.n) + ">"

    # define "*"
    def __mul__(self, other):
        try:
            if self.n == other.n:
                return TwistedInt((self.object + other.object + self.object * other.object) % self.n, self.n)
            else:
                raise MismatchedModException
        except MismatchedModException:
            return "Cannot multiply two values with different mods"

    # define "+"
    def __add__(self, other):
        try:
            if self.n == other.n:
                return TwistedInt((self.object + other.object) % self.n, self.n)
            else:
                raise MismatchedModException
        except MismatchedModException:
            return "Cannot add two values with different mods"

    # Easy Requirement 1
    # Returns set (in form of a list) of twisted ints that return 1 when multiplied
    # by themselves for each set of n -> upperN
    # TODO add counter for each valid value for each n
    @staticmethod
    def mulEqualToOne(upperN):
        validInts = []

        for n in range(1, upperN + 1):
            for i in range(n):
                x = TwistedInt(i, n)

                if (x * x).object == 1:
                    validInts.append(str(x))

        return validInts
