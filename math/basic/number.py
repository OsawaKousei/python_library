import abc


class Number(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        self._type = "number"
        self.check()
        self.standardize()

    @property
    def type(self):
        return self._type

    @abc.abstractmethod
    def __str__(self):
        pass

    def show(self):
        print(self.__str__())

    @abc.abstractmethod
    def standardize(self):
        pass

    @abc.abstractmethod
    def check(self):
        pass

    @abc.abstractmethod
    def get_numerical_value(self):
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

    @abc.abstractmethod
    def __truediv__(self, other):
        pass
