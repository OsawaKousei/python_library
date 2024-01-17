from fraction import fraction as fl
import random


class simple_exponents:
    def __init__(self, base, exponent):
        fl.check(base)
        self.base = base
        fl.check(exponent)
        self.exponent = exponent

    def standardize(self):
        return self

    def get_factor(self):
        return self.base, self.exponent

    def get_string(self):
        return "(" + fl.get_string(self.base) + "^" + fl.get_string(self.exponent) + ")"

    def show(self):
        print(simple_exponents.get_string(self))


class simple_exponents_test:
    def __init__(self):
        pass

    @staticmethod
    def random_exponents():
        e = simple_exponents(random.randint(1, 100), random.randint(1, 3))
        e.show()
        return e

    @staticmethod
    def arbitrary_exponents():
        print("input base numerator")
        base_numerator = int(input())
        print("input base denominator")
        base_denominator = int(input())
        print("input exponent numerator")
        exponent_numerator = int(input())
        print("input exponent denominator")
        exponent_denominator = int(input())
        e = simple_exponents(
            fl(base_numerator, base_denominator),
            fl(exponent_numerator, exponent_denominator),
        )
        e.show()


simple_exponents_test.random_exponents()
simple_exponents_test.arbitrary_exponents()
