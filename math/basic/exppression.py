import abc
from binary_tree import Binary_tree as Bt
from integer import Integer as Intg


class Expression(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        self._type = "expression"
        self.cont = Bt(Intg(0))
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


class Operator:
    def __init__(self, op):
        self._op = op
        self._type = "operator"

    @property
    def type(self):
        return self._type

    @property
    def op(self):
        return self._op

    def __str__(self):
        return self.op.__str__()
