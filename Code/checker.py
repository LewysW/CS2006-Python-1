"""Checks whether or not for a given n the following properties hold for all x, y, z ∈ Zn:"""

from twisted_int import *

#TODO throw exceptions for negatives
def isCommutativeAdd(n):
    """Tests that x ⊕ y = y ⊕ x for all x, y, z ∈ Zn

    Tests for every value under n, ignoring duplicates.
    e.g. Once <0:n> + <1:n>  = <1:n> + <0:n> has been confirmed,
    no need to test <1:n> + <0:n> = <0:n> + <1:n>
    """
    numList = [x for x in range(n)]
    numStr = ''.join(str(y) for y in numList)

    for nums in itertools.combinations_with_replacement(numStr,2):
        x = int(nums[0])
        y = int(nums[1])
        a = TwistedInt(x, n)
        b = TwistedInt(y, n)
        print(str(a) + " + " + str(b))

        if (a + b).object != (b + a).object:
            return False

    return True

def isCommutativeMul(n):
    """Tests x ⊗ y = y ⊗ x for all x, y, z ∈ Zn
    
    Tests for every value under n, ignoring duplicates.
    e.g. Once <0:n> * <1:n>  = <1:n> * <0:n> has been confirmed,
    no need to test <1:n> * <0:n> = <0:n> * <1:n>"""

    numList = [x for x in range(n)]
    numStr = ''.join(str(y) for y in numList)

    for nums in itertools.combinations_with_replacement(numStr,2):
        x = int(nums[0])
        y = int(nums[1])
        a = TwistedInt(x, n)
        b = TwistedInt(y, n)
        print(str(a) + " * " + str(b))

        if (a * b).object != (b * a).object:
            return False

    return True

def isCommutativePrecedenceAdd(n):
    """Tests (x ⊕ y) ⊕ z = x ⊕ (y ⊕ z)"""

    numList = [x for x in range(n)]
    numStr = ''.join(str(y) for y in numList)

    for nums in itertools.combinations_with_replacement(numStr,3):
        x = int(nums[0])
        y = int(nums[1])
        z = int(nums[2])
        a = TwistedInt(x, n)
        b = TwistedInt(y, n)
        c = TwistedInt(z, n)
        print("(" + str(a) + " + " + str(b) + ") + " + str(c))

        if ((a + b) + c).object != (a + (b + c)).object:
            return False

    return True

def isCommutativePrecedenceMul(n):
    """Tests (x ⊗ y) ⊗ z = x ⊗ (y ⊗ z)"""

    numList = [x for x in range(n)]
    numStr = ''.join(str(y) for y in numList)

    for nums in itertools.combinations_with_replacement(numStr,3):
        x = int(nums[0])
        y = int(nums[1])
        z = int(nums[2])
        a = TwistedInt(x, n)
        b = TwistedInt(y, n)
        c = TwistedInt(z, n)
        print("(" + str(a) + " * " + str(b) + ") * " + str(c))

        if ((a * b) * c).object != (a * (b * c)).object:
            return False

    return True

def isCommutativeCommonFac(n):
    """Tests (x ⊕ y) ⊗ z = (x ⊗ z) ⊕ (y ⊗ z)"""

    numList = [x for x in range(n)]
    numStr = ''.join(str(y) for y in numList)

    for nums in itertools.combinations_with_replacement(numStr,3):
        x = int(nums[0])
        y = int(nums[1])
        z = int(nums[2])
        a = TwistedInt(x, n)
        b = TwistedInt(y, n)
        c = TwistedInt(z, n)
        print("(" + str(a) + " + " + str(b) + ") * " + str(c))

        if ((a + b) * c).object != ((a * c) + (b * c)).object:
            return False

    return True
