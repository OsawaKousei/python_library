import abc


class Number(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        self.type = "number"

    @abc.abstractmethod
    def __str__(self):
        pass

    def show(self):
        print(self.__str__())

    @abc.abstractmethod
    def standardize(self):
        pass

    @abc.abstractmethod
    def get_type(self):
        pass

    @abc.abstractmethod
    def check(self):
        pass

    @abc.abstractmethod
    def get_value(self):
        pass

    @abc.abstractmethod
    def get_factor(self):
        pass

    @abc.abstractmethod
    @staticmethod
    def __add__(n1, n2):
        pass

    @abc.abstractmethod
    @staticmethod
    def __sub__(n1, n2):
        pass

    @abc.abstractmethod
    @staticmethod
    def __mul__(n1, n2):
        pass

    @abc.abstractmethod
    @staticmethod
    def __truediv__(n1, n2):
        pass
