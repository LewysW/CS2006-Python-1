"""Checks whether or not for a given n the following properties hold for all x, y, z ∈ Zn:"""

from twisted_int import *

def isCommutativeAdd(n):
    """Tests x ⊕ y = y ⊕ x"""

    xlist = ylist = [x for x in range(0, n)]

    for x, y in itertools.product(xlist, ylist):
        a = TwistedInt(x, n)
        b = TwistedInt(y, n)

        if (a + b).object != (b + a).object:
            return False

    return True

def isCommutativeMul(n):
    """Tests x ⊗ y = y ⊗ x """

    xlist = ylist = [x for x in range(0, n)]

    for x, y in itertools.product(xlist, ylist):
        a = TwistedInt(x, n)
        b = TwistedInt(y, n)

        if (a * b).object != (b * a).object:
            return False

    return True

def isCommutativePrecedenceAdd(n):
    """Tests (x ⊕ y) ⊕ z = x ⊕ (y ⊕ z)"""

    xlist = ylist = zlist = [x for x in range(0, n)]

    for x, y, z in itertools.product(xlist, ylist, zlist):
        a = TwistedInt(x, n)
        b = TwistedInt(y, n)
        c = TwistedInt(z, n)

        if ((a + b) + c).object != (a + (b + c)).object:
            return False

    return True

def isCommutativePrecedenceMul(n):
    """Tests (x ⊗ y) ⊗ z = x ⊗ (y ⊗ z)"""

    xlist = ylist = zlist = [x for x in range(0, n)]

    for x, y, z in itertools.product(xlist, ylist, zlist):
        a = TwistedInt(x, n)
        b = TwistedInt(y, n)
        c = TwistedInt(z, n)

        if ((a * b) * c).object != (a * (b * c)).object:
            return False

    return True

def isCommutativeCommonFac(n):
    """Tests (x ⊕ y) ⊗ z = (x ⊗ z) ⊕ (y ⊗ z)"""

    xlist = ylist = zlist = [x for x in range(0, n)]

    for x, y, z in itertools.product(xlist, ylist, zlist):
        a = TwistedInt(x, n)
        b = TwistedInt(y, n)
        c = TwistedInt(z, n)

        if ((a + b) * c).object != ((a * c) + (b * c)).object:
            return False

    return True