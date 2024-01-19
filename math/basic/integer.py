from number import Number


class Integer(Number):
    def __init__(self, value):
        self.value = value
        super().__init__()
        self._type = "integer"

    def __str__(self):
        return str(self.value)

    def standardize(self):
        return self

    def check(self):
        if type(self.value) != int:
            raise TypeError("value is not an integer")

    def get_numerical_value(self):
        return self.value

    def __add__(self, other):
        return Integer(self.value + other.value)

    def __sub__(self, other):
        return Integer(self.value - other.value)

    def __mul__(self, other):
        return Integer(self.value * other.value)

    def __truediv__(self, other):
        if self.value % other.value != 0:
            raise ValueError(str(self) + " is not divisible by " + str(other))

        return Integer(self.value // other.value)

    def __mod__(self, other):
        return Integer(self.value % other.value)


class Integer_test:
    def __init__(self) -> None:
        pass

    @staticmethod
    def instantiate_integer():
        a = Integer(1)
        b = Integer(2)
        c = Integer(3)
        print(a)
        print(b)
        print(c)

    @staticmethod
    def integer_operations():
        a = Integer(1)
        b = Integer(2)
        c = Integer(3)
        print(a + b)
        print(a - b)
        print(a * b)
        print(b % a)
        print(b / a)
        print(a % c)
        print(a / c)


# Integer_test.instantiate_integer()
Integer_test.integer_operations()
