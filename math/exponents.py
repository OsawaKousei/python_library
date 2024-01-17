import random
from fraction import fraction as fl
from integeral import integeral as intg


class exponents:
    def __init__(self, coeff, base, exponent):
        self.coeff = coeff
        self.base = fl.fraction(base, 1)
        self.exponent = fl.fraction(exponent, 1)

    def standardize(self):
        return self

    def get_factor(self):
        return self.base, self.exponent

    def get_string(self):
        return "(" + fl.get_string(self.base) + "^" + fl.get_string(self.exponent) + ")"

    def show(self):
        print(
            "(",
            fl.get_string(self.coeff),
            "×",
            fl.get_string(self.base),
            "^",
            fl.get_string(self.exponent),
            ")",
        )

    @staticmethod
    def max_exponential_divide(base, exponent):
        fl.check(base)
        fl.check(exponent)
        if exponent.numerator < 0:
            raise ValueError("exponent must be positive")
        if base.numerator < 0:
            raise ValueError("base must be positive")

    @staticmethod
    def max_exponential_divide_sub(base, exponent):
        if not type(base) == int:
            raise TypeError("base must be integer")
        if base < 0:
            raise ValueError("base must be positive")
        fl.check(exponent)
        if exponent.numerator < 0:
            raise ValueError("exponent must be positive")
        a = intg.max_exponential_divide(base, exponent.numerator)
        return exponents(
            a, base // intg.integeral_power(a, exponent.denominator), exponent.numerator
        )


class exponents_test:
    def __init__(self):
        pass

    @staticmethod
    def random_exponents_test():
        base = random.randint(-10, 10)
        exponent = random.randint(-10, 10)
        e = exponents(base, exponent)
        e.show()

    @staticmethod
    def arbitrary_exponents_test():
        print("input base")
        base = int(input())
        print("input exponent")
        exponent = int(input())
        e = exponents(base, exponent)
        e.show()

    @staticmethod
    def all_test():
        return

    def test_integral_power():
        print("input base")
        base = int(input())
        print("input exponent")
        exponent = int(input())
        print(exponents.integeral_power(base, exponent))

    def test_expontial_divide_sub():
        print("input base")
        base = int(input())
        print("input exponent")
        exponent = int(input())
        exponents.max_exponential_divide_sub(base, exponent)
