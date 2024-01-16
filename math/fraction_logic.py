# 分数クラス
class fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def get_numerical_factor(self):
        return self.numerator, self.denominator

    @staticmethod
    def reciprocal(fraction):
        return fraction(fraction.denominator, fraction.numerator)

    @staticmethod
    def gcd(a, b):
        while b:  # while文では0以外の値はTrueとして扱われる
            a, b = b, a % b
        return a

    @staticmethod
    def lcm(a, b):
        return a * b // fraction.gcd(a, b)  # //は整数除算

    @staticmethod
    def reduce(numerator, denominator):
        gcd = fraction.gcd(numerator, denominator)
        return numerator // gcd, denominator // gcd

    @staticmethod
    def add(f1numerator, f1denominator, f2numerator, f2denominator):
        lcm = fraction.lcm(f1denominator, f2denominator)
        f1numerator *= lcm // f1denominator
        f2numerator *= lcm // f2denominator
        return fraction.reduce(f1numerator + f2numerator, lcm)

    @staticmethod
    def sub(f1numerator, f1denominator, f2numerator, f2denominator):
        lcm = fraction.lcm(f1denominator, f2denominator)
        f1numerator *= lcm // f1denominator
        f2numerator *= lcm // f2denominator
        return fraction.reduce(f1numerator - f2numerator, lcm)

    @staticmethod
    def mul(f1numerator, f1denominator, f2numerator, f2denominator):
        return fraction.reduce(f1numerator * f2numerator, f1denominator * f2denominator)

    @staticmethod
    def div(f1numerator, f1denominator, f2numerator, f2denominator):
        return fraction.reduce(f1numerator * f2denominator, f1denominator * f2numerator)
