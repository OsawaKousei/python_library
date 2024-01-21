import abc
from binary_tree import Binary_tree as Bt


class Expression(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        self._type = "expression"
        self.cont = Bt(0)
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
    def term_check(self):
        pass

    @abc.abstractmethod
    def check(self):
        pass
