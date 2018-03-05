"""Easy tasks 1 & 2"""

from twisted_int import *
from itertools import combinations_with_replacement
from itertools import product

# EASY REQUIREMENT 1

# TODO add counter for each valid value for each n
def mulEqualToOne(n):
    """Returns a list of TwistedInts that return 1 when multiplied by themselves for the set Zn

    For every value under n, iterates through values to find TwistedInts, checking to see if they return 1 when squared.
    All valid TwistedInts are returned as a List

    Args:
        n: value for use in finding Zn. (tests for all values under n)

    Returns:
        list: containing all valid TwistedInts according to criteria

    Examples:
        >>> mulEqualToOne(3)
        ['<1:2>']
        >>> mulEqualToOne(10)
        ['<1:2>', '<2:7>', '<3:7>']
        >>> mulEqualToOne(0)
        []
    """

    if type(n) is str:
        raise TypeError("argument (Mod) must be an int")
    if n < 0:
        raise InvalidModError("argument (Mod) must be greater than 0")

    validInts = []

    for mod in range(1, n + 1):
        for val in range(mod):
            x = TwistedInt(val, mod)

            if (x * x).object == 1:
                validInts.append(str(x))

    return validInts

# EASY REQUIREMENT 2

#TODO throw exceptions for negatives
def isCommutativeAdd(n):
    """Tests that x ⊕ y = y ⊕ x for all x, y, z ∈ Zn

    Tests for every value under n, ignoring duplicates.
    Once <0:n> + <1:n>  = <1:n> + <0:n> has been confirmed,
    no need to test <1:n> + <0:n> = <0:n> + <1:n>

    Args:
        n: value for use in finding Zn. (tests for all values under n)

    Returns:
        bool: True if true for all values, False otherwise

    Examples:
        >>> isCommutativeAdd(2)
        <0:2> <0:2>
        <0:2> <1:2>
        <1:2> <1:2>
        True
    """
                # iterates through all combinations of numbers in range
    for nums in combinations_with_replacement(range(n), 2):
                # creates new twisted integers
        x = int(nums[0]); a = TwistedInt(x, n)
        y = int(nums[1]); b = TwistedInt(y, n)
        print(str(a) + " " + str(b))
                # tests them
        if (a + b).object != (b + a).object:
            return False

    return True


def isCommutativeMul(n):
    """Tests x ⊗ y = y ⊗ x for all x, y, z ∈ Zn

    Tests for every value under n, ignoring duplicates.
    Once <0:n> * <1:n>  = <1:n> * <0:n> has been confirmed,
    no need to test <1:n> * <0:n> = <0:n> * <1:n>

    Args:
        n: value for use in finding Zn. (tests for all values under n)

    Returns:
        bool: True if true for all values, False otherwise

    Examples:
        >>> isCommutativeMul(2)
        <0:2> <0:2>
        <0:2> <1:2>
        <1:2> <1:2>
        True
    """
                # iterates through all combinations of numbers in range
    for nums in combinations_with_replacement(range(n), 2):
                # creates new twisted ints
        x = int(nums[0]); a = TwistedInt(x, n)
        y = int(nums[1]); b = TwistedInt(y, n)
        print(str(a) + " " + str(b))
                # tests them
        if (a * b).object != (b * a).object:
            return False

    return True


def isCommutativePrecedenceAdd(n):
    """Tests (x ⊕ y) ⊕ z = x ⊕ (y ⊕ z)

    Tests for every value under n.
    Ignoring duplicates is harder here so they are currently not ignored.

    Args:
        n: value for use in finding Zn. (tests for all values under n)

    Returns:
        bool: True if true for all values, False otherwise

    Examples:
        >>> isCommutativePrecedenceAdd(2)
        <0:2> <0:2> <0:2>
        <0:2> <0:2> <1:2>
        <0:2> <1:2> <0:2>
        <0:2> <1:2> <1:2>
        <1:2> <0:2> <0:2>
        <1:2> <0:2> <1:2>
        <1:2> <1:2> <0:2>
        <1:2> <1:2> <1:2>
        True
    """
                # iterates through all combinations of 3 values in range
    for nums in getAllCombinations(n, 3):
                # creates twisted ints
        x = int(nums[0]); a = TwistedInt(x, n)
        y = int(nums[1]); b = TwistedInt(y, n)
        z = int(nums[2]); c = TwistedInt(z, n)
        print(str(a) + " " + str(b) + " " + str(c))
                # tests them
        if ((a + b) + c).object != (a + (b + c)).object:
            return False

    return True


def isCommutativePrecedenceMul(n):
    """Tests (x ⊗ y) ⊗ z = x ⊗ (y ⊗ z)

    Tests for every value under n.
    Ignoring duplicates is not done to the same level here, as with 3 values, the possible combinations is much greater.

    Args:
        n: value for use in finding Zn. (tests for all values under n)

    Returns:
        bool: True if true for all values, False otherwise

    Examples:
        >>> isCommutativePrecedenceMul(2)
        <0:2> <0:2> <0:2>
        <0:2> <0:2> <1:2>
        <0:2> <1:2> <0:2>
        <0:2> <1:2> <1:2>
        <1:2> <0:2> <0:2>
        <1:2> <0:2> <1:2>
        <1:2> <1:2> <0:2>
        <1:2> <1:2> <1:2>
        True
    """
                # iterates through all combinations of 3 values in range
    for nums in getAllCombinations(n, 3):
                # creates twisted ints
        x = int(nums[0]); a = TwistedInt(x, n)
        y = int(nums[1]); b = TwistedInt(y, n)
        z = int(nums[2]); c = TwistedInt(z, n)
        print(str(a) + " " + str(b) + " " + str(c))
                # tests them
        if ((a * b) * c).object != (a * (b * c)).object:
            return False

    return True


def isCommutativeCommonFac(n):
    """Tests (x ⊕ y) ⊗ z = (x ⊗ z) ⊕ (y ⊗ z)

    Tests for every value under n.
    Ignoring duplicates is harder here so they are currently not ignored.

    Args:
        n: value for use in finding Zn. (tests for all values under n)

    Returns:
        bool: True if true for all values, False otherwise

    Examples:
        >>> isCommutativeCommonFac(2)
        <0:2> <0:2> <0:2>
        <0:2> <0:2> <1:2>
        <0:2> <1:2> <0:2>
        <0:2> <1:2> <1:2>
        <1:2> <0:2> <0:2>
        <1:2> <0:2> <1:2>
        <1:2> <1:2> <0:2>
        <1:2> <1:2> <1:2>
        True
    """
                # iterates through all combinations of 3 values in range
    for nums in getAllCombinations(n, 3):
                # creates twisted ints
        x = int(nums[0]); a = TwistedInt(x, n)
        y = int(nums[1]); b = TwistedInt(y, n)
        z = int(nums[2]); c = TwistedInt(z, n)
        print(str(a) + " " + str(b) + " " + str(c))
                # tests them
        if ((a + b) * c).object != ((a * c) + (b * c)).object:
            return False

    return True


def getAllCombinations(n, r):
    """Returns a sorted list of all the possible combinations of the numbers under a value.

    Args:
        n: the value to find combinations under
        r: the number of combinations of values to find

    Returns:
        a set of all combinations

    Examples:
        >>> getAllCombinations(2,3)
        [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]

        >>> getAllCombinations(3,2)
        [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    """
    numList = set(product(range(n), repeat = r))
    return sorted(numList)
