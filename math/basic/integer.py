from number import Number


class Integer(Number):
    def __init__(self, value):
        self._value = int(value)  # int()を用いないと初期化時のcheck()でエラーが出る
        super().__init__()
        self._type = "integer"

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return self.value

    def standardize(self):
        return self

    @property
    def value(self):
        return self._value

    def check(self):
        if type(self) != Integer:
            if type(self) == int:
                self = Integer(self)
            else:
                raise TypeError("This variable cannot be interpreted as an integer.")
        if type(self.value) != int:
            raise ValueError(
                "This variable has an illegal value that is not an integer"
            )

        return self

    def get_numerical_value(self):
        return self.value

    def __eq__(self, other):
        try:
            other = Integer.check(other)
        except TypeError:
            return False

        return self.value == other.value

    def __ne__(self, other):
        try:
            other = Integer.check(other)
        except TypeError:
            return True

        return self.value != other.value

    def __lt__(self, other):
        try:
            other = Integer.check(other)
        except TypeError:
            raise TypeError("cannot compare Integer with " + str(type(other)))

        return self.value < other.value

    def __gt__(self, other):
        try:
            other = Integer.check(other)
        except TypeError:
            raise TypeError("cannot compare Integer with " + str(type(other)))

        return self.value > other.value

    def __add__(self, other):
        try:
            return Integer(self.value + Integer.check(other).value)
        except TypeError:
            raise TypeError("cannot add Integer with " + str(type(other)))

    def __sub__(self, other):
        try:
            return Integer(self.value - Integer.check(other).value)
        except TypeError:
            raise TypeError("cannot subtract Integer with " + str(type(other)))

    def __mul__(self, other):
        try:
            return Integer(self.value * Integer.check(other).value)
        except TypeError:
            raise TypeError("cannot multiply Integer with " + str(type(other)))

    def __truediv__(self, other):
        try:
            other = Integer.check(other)
            if other.value == 0:
                raise ValueError("can not divisible by 0")
            if self.value % other.value != 0:
                raise ValueError(
                    str(self.value) + " is not divisible by " + str(other.value)
                )
            return Integer(self.value / other.value)
        except TypeError:
            raise TypeError("cannot divide Integer with " + str(type(other)))

    def __mod__(self, other):
        try:
            other = Integer.check(other)
            if other.value == 0:
                raise ValueError("can not divisible by 0")
            return Integer(self.value % other.value)
        except TypeError:
            raise TypeError("cannot modulo Integer with " + str(type(other)))

    def __pow__(self, other):
        try:
            return Integer(self.value ** Integer.check(other).value)
        except TypeError:
            raise TypeError("cannot power Integer with " + str(type(other)))

    @staticmethod
    def gcd(a, b):
        if type(a) != Integer or type(b) != Integer:
            raise TypeError("gcd function only accepts integers")
        while b != 0:
            a, b = b, a % b
        return a

    @staticmethod
    def lcm(a, b):
        if type(a) != Integer or type(b) != Integer:
            raise TypeError("lcm function only accepts integers")
        return a * b / Integer.gcd(a, b)


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
        print(a**b)
        print(a**c)
        # print(a / c) # ValueError: 1 is not divisible by 3

    @staticmethod
    def gcd_test():
        a = Integer(10)
        b = Integer(12)
        c = Integer(60)
        print(Integer.gcd(a, b))
        print(Integer.gcd(a, c))
        print(Integer.gcd(b, c))

    @staticmethod
    def lcm_test():
        a = Integer(1)
        b = Integer(2)
        c = Integer(3)
        print(Integer.lcm(a, b))
        print(Integer.lcm(a, c))
        print(Integer.lcm(b, c))


# Integer_test.instantiate_integer()
# Integer_test.integer_operations()
# Integer_test.gcd_test()
# Integer_test.lcm_test()

""" memo
どちらも可能
a = Integer(1)
print(a.check())
print(Integer.check(a))
"""


""" memo
a = Integer(1)
b = 2

print(a + b) #AttributeError: 'int' object has no attribute 'value'
print(b + a) # TypeError: unsupported operand type(s) for +: 'int' and 'Integer'
"""
