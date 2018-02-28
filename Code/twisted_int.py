class TwistedInt:

    def __init__(self, obj, mod):
        self.object = obj
        self.mod = mod

    # overwrite "print"
    def __str__(self):
        return "<" + str(self.object)+ ":" + str(self.mod) + ">"

    # define "*"
    def __mul__(self, other):
        try:
            if self.mod == other.mod:
                return TwistedInt((self.object + other.object + self.object * other.object) % self.mod, self.mod)
            else:
                raise ValueError
        except ValueError:
            return "Cannot multiply two values with different mods"


    # define "+"
    def __add__(self, other):
        try:
            if self.mod == other.mod:
                return TwistedInt((self.object + other.object) % self.mod, self.mod)
            else:
                raise ValueError
        except ValueError:
            return "Cannot add two values with different mods"
