import abc


class Ring(metaclass=abc.ABCMeta):  # 抽象クラス　環
    @abc.abstractmethod
    def __init__(self, name):
        self.name = name
        self.type = "ring"

    @abc.abstractmethod
    def __str__(self):
        pass

    @abc.abstractmethod
    def __add__(self, other):
        pass

    @abc.abstractmethod
    def __sub__(self, other):
        pass

    @abc.abstractmethod
    def __mul__(self, other):
        pass


class Field(Ring, metaclass=abc.ABCMeta):  # 抽象クラス　体、環を継承して除法を追加
    @abc.abstractmethod
    def __init__(self, name):
        super().__init__(name)
        self.type = "field"

    @abc.abstractmethod
    def __truediv__(self, other):
        pass


class Int_ring(Ring):  # 整数環
    def __init__(self, name, value):
        super().__init__(name)
        self.value = value

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        return Int_ring(self.name, self.value + other.value)

    def __sub__(self, other):
        return Int_ring(self.name, self.value - other.value)

    def __mul__(self, other):
        return Int_ring(self.name, self.value * other.value)


def int_ring_test():
    int_ring = Int_ring("test", 1)
    int_ring2 = Int_ring("test2", 2)
    print(int_ring + int_ring2)
    print(int_ring - int_ring2)
    print(int_ring * int_ring2)


int_ring_test()


class Rational_field(Field):  # 有理数体、体を継承して全ての演算を定義
    def __init__(self, name, value):
        super().__init__(name)
        self.value = value

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        return Int_ring(self.name, self.value + other.value)

    def __sub__(self, other):
        return Int_ring(self.name, self.value - other.value)

    def __mul__(self, other):
        return Int_ring(self.name, self.value * other.value)

    def __truediv__(self, other):
        return Int_ring(self.name, self.value / other.value)


def rational_field_test():
    rational_field = Rational_field("test", 1)
    rational_field2 = Rational_field("test2", 2)
    print(rational_field + rational_field2)
    print(rational_field - rational_field2)
    print(rational_field * rational_field2)
    print(rational_field / rational_field2)


rational_field_test()


class Rational_field2(Field, Int_ring):  # 有理数体、体と整数環を多重継承して、除法のみ定義
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __truediv__(self, other):
        return Int_ring(self.name, self.value / other.value)


def rational_field2_test():
    rational_field = Rational_field2("test", 1)
    rational_field2 = Rational_field2("test2", 2)
    print(rational_field + rational_field2)
    print(rational_field - rational_field2)
    print(rational_field * rational_field2)
    print(rational_field / rational_field2)


rational_field2_test()
