from twisted_int import *

#Easy Requirement 2.1
def isCommutativeAdd(n):
    xlist = ylist = [x for x in range(0, n)]

    for x, y in itertools.product(xlist, ylist):
        a = TwistedInt(x, n)
        b = TwistedInt(y, n)

        if (a + b).object != (b + a).object:
            return False

    return True

    #Easy Requirement 2.2
@staticmethod
def isCommutativeMul(n):
    xlist = ylist = [x for x in range(0, n)]

    for x, y in itertools.product(xlist, ylist):
        a = TwistedInt(x, n)
        b = TwistedInt(y, n)

        if (a * b).object != (b * a).object:
            return False

    return True

#Easy Requirement 2.3
@staticmethod
def isCommutativePrecedenceAdd(n):
    xlist = ylist = zlist = [x for x in range(0, n)]

    for x, y, z in itertools.product(xlist, ylist, zlist):
        a = TwistedInt(x, n)
        b = TwistedInt(y, n)
        c = TwistedInt(z, n)

        if ((a + b) + c).object != (a + (b + c)).object:
            return False

    return True

#Easy Requirement 2.4
@staticmethod
def isCommutativePrecedenceMul(n):
    xlist = ylist = zlist = [x for x in range(0, n)]

    for x, y, z in itertools.product(xlist, ylist, zlist):
        a = TwistedInt(x, n)
        b = TwistedInt(y, n)
        c = TwistedInt(z, n)

        if ((a * b) * c).object != (a * (b * c)).object:
            return False

    return True

#Easy Requirement 2.5
@staticmethod
def isCommutativeCommonFac(n):
    xlist = ylist = zlist = [x for x in range(0, n)]

    for x, y, z in itertools.product(xlist, ylist, zlist):
        a = TwistedInt(x, n)
        b = TwistedInt(y, n)
        c = TwistedInt(z, n)

        if ((a + b) * c).object != ((a * c) + (b * c)).object:
            return False

    return True
