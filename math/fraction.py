import random
from integeral import integeral as intg


class fraction:  # 分数クラス
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        if denominator == 0:
            raise ValueError("denominator must not be 0")
        self.denominator = denominator
        self.standardize()
        fraction.reduce(self)

    def standardize(self):
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1
        return self

    def get_factor(self):
        return self.numerator, self.denominator

    def get_string(self):
        return self.numerator.__str__() + "/" + self.denominator.__str__()

    def show(self):
        print(self.numerator, "/", self.denominator)

    @staticmethod
    def check(f):
        if not hasattr(f, "numerator") or not hasattr(f, "denominator"):
            raise TypeError("this variable must be fraction")

    @staticmethod
    def reciprocal(f):
        fraction.check(f)
        return fraction(f.denominator, f.numerator)

    @staticmethod
    def reduce(f):
        fraction.check(f)
        gcd = intg.gcd(f.numerator, f.denominator)
        f.numerator //= gcd
        f.denominator //= gcd
        return f

    @staticmethod
    def add(f1, f2):
        fraction.check(f1)
        fraction.check(f2)
        lcm = fraction.lcm(f1.denominator, f2.denominator)
        return fraction(
            f1.numerator * lcm // f1.denominator + f2.numerator * lcm // f2.denominator,
            lcm,
        )

    @staticmethod
    def sub(f1, f2):
        fraction.check(f1)
        fraction.check(f2)
        lcm = fraction.lcm(f1.denominator, f2.denominator)
        return fraction(
            f1.numerator * lcm // f1.denominator - f2.numerator * lcm // f2.denominator,
            lcm,
        )

    @staticmethod
    def mul(f1, f2):
        fraction.check(f1)
        fraction.check(f2)
        return fraction(f1.numerator * f2.numerator, f1.denominator * f2.denominator)

    @staticmethod
    def div(f1, f2):
        fraction.check(f1)
        fraction.check(f2)
        return fraction.mul(f1, fraction.reciprocal(f2))


class fraction_test:  # 分数テストクラス
    def __init__(self):
        pass

    @staticmethod
    def random_fraction():
        numerator = random.randint(-100, 100)
        denominator = random.randint(-100, 100)
        return fraction(numerator, denominator)

    @staticmethod
    def arbitrary_fraction():
        print("input numerator")
        numerator = int(input())
        print("input denominator")
        denominator = int(input())
        return fraction(numerator, denominator)

    @staticmethod
    def all_test(f1, f2):
        print("reciprocal fraction1:")
        fraction.reciprocal(f1).show()
        print(
            "add"
            + f1.numerator.__str__()
            + "/"
            + f1.denominator.__str__()
            + "+"
            + f2.numerator.__str__()
            + "/"
            + f2.denominator.__str__()
            + ":"
        )
        fraction.add(f1, f2).show()
        print(
            "sub"
            + f1.numerator.__str__()
            + "/"
            + f1.denominator.__str__()
            + "-"
            + f2.numerator.__str__()
            + "/"
            + f2.denominator.__str__()
            + ":"
        )
        fraction.sub(f1, f2).show()
        print(
            "mul"
            + f1.numerator.__str__()
            + "/"
            + f1.denominator.__str__()
            + "×"
            + f2.numerator.__str__()
            + "/"
            + f2.denominator.__str__()
            + ":"
        )
        fraction.mul(f1, f2).show()
        print(
            "div"
            + f1.numerator.__str__()
            + "/"
            + f1.denominator.__str__()
            + "÷"
            + f2.numerator.__str__()
            + "/"
            + f2.denominator.__str__()
            + ":"
        )
        fraction.div(f1, f2).show()

    @staticmethod
    def random_fraction_test():
        f1 = fraction_test.random_fraction()
        f2 = fraction_test.random_fraction()
        print("fraction1:")
        f1.show()
        print("fraction2:")
        f2.show()

        fraction_test.all_test(f1, f2)

    @staticmethod
    def arbitrary_fraction_test():
        f1 = fraction_test.arbitrary_fraction()
        f2 = fraction_test.arbitrary_fraction()
        print("fraction1:")
        f1.show()
        print("fraction2:")
        f2.show()

        fraction_test.all_test(f1, f2)
