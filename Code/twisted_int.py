class TwistedInt:

    def __init__(self, obj):
        self.object = obj

    # overwrite "print"
    def __str__(self):
        return "<"+str(self.object)+">"

    # define "*"
    def __mul__(self, other):
        return TwistedInt(self.object + other.object + self.object * other.object)

    def hello(self):
        return "Hello, World!"
