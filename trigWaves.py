import math

class SinWave:
    def __init__(self, a, b, c, d, minV, maxV):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        self.minV = minV
        self.maxV = maxV

        if not self.c:
            self.findC()

    def calcY(self, x):
        return (self.a * math.sin(self.b * (x + self.c))) + self.d

    def calcX(self, y):
        return ((math.asin((y - self.d) / self.a)) / self.b) - self.c

    def findC(self):
        diff = self.minV[1] - self.calcX(self.minV[1])
        self.c = diff
        return self.c


    def __repr__(self):
        return '{} sin ({}(x + {})) + {}'.format(self.a, self.b, self.c, self.d)

    def __call__(self, value):
        return self.calcY(value)

