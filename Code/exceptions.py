class InvalidModException(Exception):
   """Invalid mod value"""

class InvalidObjException(Exception):
    """Invalid obj value"""

class InvalidTypeException(Exception):
    """Expected Int""" # currently unused

class MismatchedModException(Exception):
    """TwistedInts have different mod values"""