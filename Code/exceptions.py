class InvalidModError(Exception):
   """Exception raised for an invalid Mod value"""
   pass

class InvalidValError(Exception):
    """Exception raised for an invalid Value input"""
    pass

class MismatchedModError(Exception):
    """Exception raised when TwistedInts have different mod values""" 
    pass

class MatrixIndexError(Exception):
    """Exception raised when the given size of a matrix does not match the contents of the matrix"""
    pass

class MismatchedMatrixError(Exception):
    """Exception raised when the size of multiple matrixes do not match when performing opperations between them"""
    pass