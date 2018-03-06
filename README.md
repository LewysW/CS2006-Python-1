# CS2006-Python-1
Group repository for first Python practical of CS2006

# Running the python code

running

    >>> from main import *

will import everything needed to run the program.

#

Check the docStrings and other documentation for more info on running functions.

# Testing

Tests have been included as DocTests. These can be run in the terminal with (for example)

    $ python twisted_int.py -v

The results of these have been stored in the file docTest results.txt. As you can see, one of these tests fails.

There should be lots of unit tests. There isn't really

# Known Bugs

# 1
getPossibleMatrices

    >>> a = TwistedInt(1,2)
    >>> aa = TwistedIntMatrix(2, 2, [a, a, a, a])
    >>> list = getPossibleMatrices([aa, aa])
    >>> for m in list:
    ...     print(m)
    <0:2> <0:2>  
    <0:2> <0:2> 

Actually returns

    <0:2> <0:2> 
    <0:2> <0:2> 
    <0:2> <0:2> 
    <0:2> <0:2> 

# 2
Matrix addition with another matrix is unimplemented

# Other
do unit testing
personal report

Lewys TODO
group report
personal report
random matrix generator
change maths to good maths characters