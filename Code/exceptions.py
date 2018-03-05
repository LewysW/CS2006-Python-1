class InvalidModError(Exception):
   """Exception raised for an invalid Mod value"""
   pass

class InvalidValError(Exception):
    """Exception raised for an invalid Value input"""
    pass

class MismatchedModError(Exception):
    """Exception raised when TwistedInts have different mod values""" 
    pass