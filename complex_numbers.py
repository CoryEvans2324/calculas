from math import *

def to_polar(c: complex):
    r = sqrt(c.real ** 2 + c.imag ** 2)
    theta = tanh(abs(c.imag) / abs(c.real))
    if c.real < 0 and c.imag >= 0:
        theta_real = pi - theta
        print('c.real < 0 and c.imag >= 0')
    elif c.real < 0 and c.imag < 0:
        theta_real = pi + theta
        print('c.real < 0 and c.imag < 0')
    elif c.real >= 0 and c.imag < 0:
        theta_real = 2 * pi - theta
        print('c.real >= 0 and c.imag < 0')
    else:
        theta_real = theta

    return r, theta_real

class ComplexPolar:
    def __init__(self, r, theta):
        self._r = r
        self._theta = theta

    @property
    def r(self):
        return self._r

    @property
    def theta(self):
        theta = self._theta % (2 * pi)
        if self._theta < 0:
            return -theta

        return theta

    @property
    def rect(self):
        return complex(self.r * cos(self.theta), self.r * sin(self.theta))

    def to_string(self, n_digits: int = 16):
        return '{} cis {}'.format(round(self.r, n_digits), round(self.theta, n_digits))

    def __repr__(self):
        return self.to_string(3)

    def __mul__(self, other):
        return ComplexPolar(self.r * other.r, self.theta + other.theat)

    def __truediv__(self, other):
        return ComplexPolar(self.r / other.r, self.theta - other.theta)

    def __pow__(self, other: int):
        return ComplexPolar(self.r ** other, self.theta * other)
