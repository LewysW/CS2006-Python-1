import sys
import unittest
import random
from twisted_int import *
from checker import *
from twisted_int_matrix import *
from twisted_integers import *


class TwistedIntTests(unittest.TestCase):

    def suite():
        loader = unittest.TestLoader()
        testsuite = loader.loadTestsFromTestCase(TwistedIntTests)
        return testsuite

    def test():
        testsuite = suite()
        runner = unittest.TextTestRunner(sys.stdout, verbosity=2)
        result = runner.run(testsuite)

    def test_NegativeInitMod(self):
        self.assertRaises(InvalidModError, TwistedInt, 5,-1)

    def test_LargerInitValue(self):
        self.assertRaises(InvalidValError, TwistedInt, 2,1)

    def test_StringMod(self):
        self.assertRaises(TypeError, TwistedInt, 2,"three")

    def test_StringValue(self):
        self.assertRaises(TypeError, TwistedInt, "two",3)

    def test_ValidInit(self):
        testTwistedInt = TwistedInt(1,2)
        self.assertEqual(testTwistedInt.object, 1)
        self.assertEqual(testTwistedInt.n, 2)

    def test_Str(self):
        self.assertEqual(str(TwistedInt(2,3)), "<2:3>")

    """def test_WrongModsMul(self):
        a = TwistedInt(1,5)
        b= TwistedInt(2,6)
        self.assertRaises(MismatchedModError, a* b)"""

    def test_ValidMul(self):
        a = TwistedInt(2,5)
        b = TwistedInt(2,5)
        self.assertEqual((a*b).object, 3)

    """def test_WrongModsAdd(self):
        a = TwistedInt(1,5)
        b = TwistedInt(2,6)
        self.assertRaises(MismatchedModError, __add__, (a,b))"""

    def test_ValidAdd(self):
        a = TwistedInt(2,5)
        b = TwistedInt(3,5)
        self.assertEqual((a + b).object, 0)

class TwistedIntegersTests(unittest.TestCase):

    def test_ValidInit(self):
        a = TwistedIntegers(2)
        self.assertEqual(print(a.integers[0]), print(TwistedInt(0,2)))
        self.assertEqual(print(a.integers[1]), print(TwistedInt(1,2)))

    def test_Str(self):
        a = TwistedIntegers(2)
        self.assertEqual(str(a), "<0:2>\n<1:2>\n")

    def test_StrEmpty(self):
        a = TwistedIntegers(0)
        self.assertEqual(str(a), "")

    def test_Size(self):
        a = TwistedIntegers(2)
        self.assertEqual(a.size(), 2)

class IteratorTests(unittest.TestCase):

    def test_ValidInit(self):
        a = TwistedIntegers(1)
        it = IteratorOfTwistedIntegers(a)
        self.assertEqual(it.index, 0)
        self.assertEqual(print(it.twistedIntegers), print(a))

    def test_HasNext(self):
        a = TwistedIntegers(2)
        it = IteratorOfTwistedIntegers(a)
        self.assertTrue(it.hasNext())

    def test_Next(self):
        a = TwistedIntegers(2)
        it = IteratorOfTwistedIntegers(a)
        self.assertEqual(print(it.next), print(it.twistedIntegers.integers[1]))

    def test_BadNext(self):
        a = TwistedIntegers(0)
        it = IteratorOfTwistedIntegers(a)
        self.assertRaises(IndexError,it.next)

    def testTauPlusEquals(self):
        self.assertEqual(['<0:100>'], tauPlusXEqualsX(100))

    def testEpsilonMulEquals(self):
        self.assertEqual(['<0:25>'], epsilonMulXEqualsX(25))

class TestChecker(unittest.TestCase):

    def test_StringMod_mulEqualToOne(self):
        self.assertRaises(TypeError, mulEqualToOne, "seven")

    def test_NegMod_mulEqualToOne(self):
        self.assertRaises(InvalidModError, mulEqualToOne, -1)

    def test_ValidMulEqualToOne(self):
        self.assertEqual(mulEqualToOne(3), ['<1:2>'])

    def testCommutativeAdd(self):
        self.assertTrue(isCommutativeAdd(5))

    def testCommutativeMul(self):
        self.assertTrue(isCommutativeMul(12))

    def testTrueCommutativePrecedenceAdd(self):
        self.assertTrue(isCommutativePrecedenceAdd(2))

    def testLargerTrueCommutativePrecedenceAdd(self):
        self.assertTrue(isCommutativePrecedenceAdd(10))

    def testCommutativePrecedenceMul(self):
        self.assertTrue(isCommutativePrecedenceMul(2))

    def testLargerTrueCommutativePrecedenceMul(self):
        self.assertTrue(isCommutativePrecedenceAdd(10))

    def testTrueCommutativeCommonFac(self):
        self.assertTrue(isCommutativeCommonFac(1))

    def testFalseCommutativeCommonFac(self):
        self.assertFalse(isCommutativeCommonFac(2))

    def testGetAllCombinations(self):
        self.assertEqual([(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)], getAllCombinations(2,3) )


class TestTwistedIntMatrix(unittest.TestCase):
    def testBadInit(self):
        self.assertRaises(IndexError, TwistedIntMatrix, 3,5,[1,2,3])

    def testBadInit(self):
        a = TwistedInt(1,6)
        b = TwistedInt(3,6)
        c = TwistedInt(4,6)
        d = TwistedInt(1,7)
        self.assertRaises(MismatchedModError, TwistedIntMatrix, 2,2,[a,b,c,d])

    def testValidInit(self):
        a = TwistedInt(1,6)
        b = TwistedInt(3,6)
        c = TwistedInt(4,6)
        d = TwistedInt(2,6)
        self.assertTrue(TwistedIntMatrix(2,2,[a,b,c,d]))

    def testStr(self):
        a = TwistedInt(1,6)
        b = TwistedInt(3,6)
        c = TwistedInt(4,6)
        d = TwistedInt(2,6)
        tim = TwistedIntMatrix(2,2,[a,b,c,d])
        self.assertEqual("<1:6> <3:6> \n<4:6> <2:6> \n", str(tim))

    """def testValueErrorMul(self):
        a = TwistedInt(1,6)
        b = TwistedInt(3,6)
        tim1 = TwistedIntMatrix(1,2,[a,b])
        c = TwistedInt(4,6)
        d = TwistedInt(2,6)
        tim2 = TwistedIntMatrix(2,1,[c,d])
        self.assertRaises(ValueError, mul, tim1,tim2)

    def testMul(self):
        a = TwistedInt(1,6)
        b = TwistedInt(3,6)
        tim1 = TwistedIntMatrix(1,2,[a,b])
        c = TwistedInt(4,6)
        d = TwistedInt(2,6)
        tim2 = TwistedIntMatrix(1,2,[c,d])
        """











if __name__ == '__main__':
    unittest.main()
