import math

# 3x^3 + 5x^2 + 6x + 9
# [3, 5, 6, 9]


class Polynomial:

    def __init__(self, *coefficients):
        self.coefficients = coefficients[::-1]

    def __repr__(self):
        return 'Polynomial ' + str(self.coefficients[::-1])

    def __call__(self, x):
        total = 0
        for index, coeff in enumerate(self.coefficients):
            total += coeff * (x ** index)
        return total


def genFactors(r):
    pairs = []
    for c in range(-r, r + 1):
        if c != 0:
            for a in range(-r, r + 1):
                pair = a / c
                if pair not in pairs:
                    pairs.append(pair)

    return pairs


c = input(
    'Input coefficients (ie "3x^3 + 5x^2 + 6x + 9" -> 3 5 6 9): ').strip().split(' ')
c = list(map(lambda x: float(x), c))
p = Polynomial(*c)


factors = []
for possibleFactor in genFactors(10):
    if p(possibleFactor) == 0:
        factors.append(possibleFactor)


if len(factors) > 0:
    for i in factors:
        print('x = ', i)

else:
    print('No factors found.')
