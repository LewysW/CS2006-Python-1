from twisted_integers import *

"""Finds valid values of τ where τ ⊕ x = x"""
def tauPlusXEqualsX(n):
    iteratorT = iteratorX = IteratorOfTwistedIntegers(TwistedIntegers(n))
    validIntegers = []
    validInt = True

    while iteratorT.hasNext():
        τ = iteratorT.next()
        iteratorX = IteratorOfTwistedIntegers(TwistedIntegers(n))

        while iteratorX.hasNext():
            x = iteratorX.next()

            if (τ + x).object != x.object:
                validInt = False
                break

        if validInt:
            validIntegers.append(str(τ))

        validInt = True

    return validIntegers

"""Finds valid values of ε where ε ⊗ x = x"""
def epsilonMulXEqualsX(n):
    iteratorE = iteratorX = IteratorOfTwistedIntegers(TwistedIntegers(n))
    validIntegers = []
    validInt = True

    while iteratorE.hasNext():
        ε = iteratorE.next()
        iteratorX = IteratorOfTwistedIntegers(TwistedIntegers(n))

        while iteratorX.hasNext():
            x = iteratorX.next()

            if (ε + x).object != x.object:
                validInt = False
                break

        if validInt:
            validIntegers.append(str(ε))

        validInt = True

    return validIntegers
