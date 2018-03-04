from twisted_integers import *

class TwistedIntMatrix:
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.matrix = []

        for i in range(0, x):
            self.matrix.append([])
            for j in range(0,y):
                self.matrix[i].append(TwistedInt(0, n))

    def __str__(self):
        out = "["

        for i in range(0, len(self.matrix)):
            out += "["
            for j in range(0, len(self.matrix[i])):
                if j > 0:
                    out += ", "
                out += str(self.matrix[i][j])

            out += "]"

        out += "]"
        return out
