from number import Number
from integer import Integer as Intg
from fraction import Fraction as Frac


class Exponents(Number):
    def __init__(self, base, exponent):
        self._base = base
        self._exponent = exponent
        super().__init__()
        self._type = "exponents"

    def __str__(self):
        return "(" + self.base.__str__() + "^" + self.exponent.__str__() + ")"

    def standardize(self):
        return self

    @property
    def base(self):
        return self._base

    @property
    def exponent(self):
        return self._exponent

    @base.setter
    def base(self, value):
        value = Frac.check(value)
        self._base = value

    @exponent.setter
    def exponent(self, value):
        value = Frac.check(value)
        self._exponent = value

    def check(self):
        if type(self) != Exponents:
            if type(self) == Frac:
                self = Exponents(self, 1)
            elif type(self) == int:
                self = Exponents(Intg(self), 1)
            else:
                raise TypeError("This variable cannot be interpreted as an exponents.")
        if type(self.base) != Frac:
            if type(self.base) == Intg:
                self.base = Frac(self.base, 1)
            else:
                raise ValueError(
                    "This base has an illegal value that is not an integer"
                )
        if type(self.exponent) != Frac:
            if type(self.exponent) == Intg:
                self.exponent = Frac(self.exponent, 1)
            else:
                raise ValueError(
                    "This exponent has an illegal value that is not an integer"
                )

        return self.standardize()

    def get_numerical_value(self):
        print("This method is not implemented yet.")

    def __eq__(self, other):
        try:
            other = Exponents.check(other)
        except TypeError:
            return False

        return self.base == other.base and self.exponent == other.exponent

    def __ne__(self, other):
        try:
            other = Exponents.check(other)
        except TypeError:
            return True

        return self.base != other.base or self.exponent != other.exponent

    def __lt__(self, other):
        print("This method is not implemented yet.")
        return False

    def __gt__(self, other):
        print("This method is not implemented yet.")
        return False

    def __add__(self, other):
        print("This method is not implemented yet.")
        return False

    def __sub__(self, other):
        print("This method is not implemented yet.")
        return False

    def __mul__(self, other):
        print("This method is not implemented yet.")
        return False

    def __truediv__(self, other):
        print("This method is not implemented yet.")
        return False


class Exponents_test:
    def __init__(self):
        pass

    def instantiate_exponents(self):
        print("=== Instantiate Exponents ===")
        exponents = Exponents(Frac(1, 2), Frac(1, 3))
        print(exponents)
        print(exponents.type)
        print(exponents.base)
        print(exponents.exponent)


# Exponents_test().instantiate_exponents()
