class Polynomial:

    def __init__(self, *coefficients):
        self.coefficients = coefficients[::-1]
        self.raw = list(coefficients)

    def __call__(self):
        return list(self.coefficients[::-1])

    def isFactor(self, x):
        total = 0
        for index, coeff in enumerate(self.coefficients):
            total += coeff * (x ** index)

        if total == 0:
            return True
        else:
            return False

    def divide(self, linear):
        poly = self.raw
        q = []
        for i in range(0, len(poly)-1):
            c = poly[i] / linear[0]
            r = c * linear[1]

            poly[i + 1] = poly[i + 1] - r
            q.append(c)

        if self.isFactor(linear[1] / linear[0]):
            return q, 0
        else:
            return q, poly[-1]


def printPoly(poly):
    out = []
    d = len(poly) - 1
    for i in poly:
        if d > 1:
            if i != 1:
                out.append(f'{i}x^{d}')
            else:
                out.append(f'x^{d}')
        elif d == 1:
            out.append(f'{i}x')
        else:
            out.append(f'{i}')

        d -= 1

    return ' + '.join(out)
