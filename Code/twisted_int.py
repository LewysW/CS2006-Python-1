class TwistedInt:

    # TODO Add validation for non int values
    # TODO Add unit tests for current functions
    # TODO move validation cod to another module
    # Validates user input.
    #Throws and exception for each different invalid piece of user input.
    def __init__(self, obj, n):
        while True:
            try:
                if n < 0:
                    raise InvalidModException
                elif obj < 0 or obj >= n:
                    raise InvalidObjException
                else:
                    self.object = obj
                    self.n = n
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
                raise InvalidModException
        except InvalidModException:
            return "Cannot multiply two values with different mods"

    # define "+"
    def __add__(self, other):
        try:
            if self.n == other.n:
                return TwistedInt((self.object + other.object) % self.n, self.n)
            else:
                raise InvalidModException
        except InvalidModException:
            return "Cannot add two values with different mods"

    # Easy Requirement 1
    # Returns set of twisted ints that return 1 when multiplied by themselves for each set of n -> upperN
    @staticmethod
    def mulEqualToOne(upperN):
        validInts = []

        for n in range(0, upperN):
            for i in range(1, n):
                x = TwistedInt(i, n)

                if str(x * x) == str(TwistedInt(1, n)):
                    validInts.append(str(x))

        return validInts

# TODO move to exception module
class InvalidModException(Exception):
    pass

class InvalidObjException(Exception):
    pass
