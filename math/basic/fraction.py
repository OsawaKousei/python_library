from number import Number
from integer import Integer as Intg


class Fraction(Number):
    def __init__(self, numerator, denominator):
        self._numerator = Intg(numerator)
        self._denominator = Intg(denominator)
        super().__init__()
        self._type = "fraction"

    def __str__(self):
        return self.numerator.__str__() + "/" + self.denominator.__str__()

    def standardize(self):
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1
        return self

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    @numerator.setter
    def numerator(self, value):
        value = Intg.check(value)
        self._numerator = value

    @denominator.setter
    def denominator(self, value):
        value = Intg.check(value)
        if value == 0:
            raise ZeroDivisionError("The denominator is zero.")
        self._denominator = value

    def check(self):
        if type(self) != Fraction:
            if type(self) == Intg:
                self = Fraction(self, 1)
            elif type(self) == int:
                self = Fraction(Intg(self), 1)
            else:
                raise TypeError("This variable cannot be interpreted as an integer.")
        if type(self.numerator) != Intg:
            raise ValueError(
                "This numerator has an illegal value that is not an integer"
            )
        if type(self.denominator) != Intg:
            raise ValueError(
                "This denominator has an illegal value that is not an integer"
            )
        if self.denominator == 0:
            raise ZeroDivisionError("The denominator is zero.")

        return self.standardize()

    def get_numerical_value(self):
        return self.numerator.__int__() / self.denominator.__int__()

    def __eq__(self, other):
        try:
            other = Fraction.check(other)
        except TypeError:
            return False

        return self.numerator * other.denominator == self.denominator * other.numerator

    def __ne__(self, other):
        try:
            other = Fraction.check(other)
        except TypeError:
            return True

        return self.numerator * other.denominator != self.denominator * other.numerator

    def __lt__(self, other):
        try:
            other = Fraction.check(other)
        except TypeError:
            raise TypeError("cannot compare Fraction with " + str(type(other)))

        self.standardize()
        other.standardize()
        # ↑分母が正であることが保証される
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __gt__(self, other):
        try:
            other = Fraction.check(other)
        except TypeError:
            raise TypeError("cannot compare Fraction with " + str(type(other)))

        self.standardize()
        other.standardize()
        # ↑分母が正であることが保証される
        return self.numerator * other.denominator > self.denominator * other.numerator

    @staticmethod
    def reciprocal(f):
        Fraction.check(f)
        return Fraction(f.denominator, f.numerator)

    @staticmethod
    def reduce(f):
        f = Fraction.check(f)
        gcd = Intg.gcd(f.numerator, f.denominator)
        f.numerator = f.numerator / gcd
        f.denominator = f.denominator / gcd
        return f

    def __add__(self, other):
        Fraction.check(self)
        Fraction.check(other)
        lcm = Intg.lcm(self.denominator, other.denominator)
        return Fraction.reduce(
            Fraction(
                self.numerator * lcm / self.denominator
                + other.numerator * lcm / other.denominator,
                lcm,
            )
        )

    def __sub__(self, other):
        Fraction.check(self)
        Fraction.check(other)
        lcm = Intg.lcm(self.denominator, other.denominator)
        return Fraction.reduce(
            Fraction(
                self.numerator * lcm / self.denominator
                - other.numerator * lcm / other.denominator,
                lcm,
            )
        )

    def __mul__(self, other):
        Fraction.check(self)
        Fraction.check(other)
        return Fraction.reduce(
            Fraction(
                self.numerator * other.numerator,
                self.denominator * other.denominator,
            )
        )

    def __truediv__(self, other):
        Fraction.check(self)
        Fraction.check(other)
        return Fraction.reduce(
            Fraction(
                self.numerator * other.denominator,
                self.denominator * other.numerator,
            )
        )


class Fraction_test:
    def __init__(self) -> None:
        pass

    @staticmethod
    def instantiate_fraction():
        a = Fraction(1, 2)
        print(a)
        a.show()

    @staticmethod
    def fraction_operations():
        a = Fraction(1, 2)
        b = Fraction(3, 4)
        print(a + b)
        print(a - b)
        print(a * b)
        print(a / b)


# Fraction_test.instantiate_fraction()
# Fraction_test.fraction_operations()
