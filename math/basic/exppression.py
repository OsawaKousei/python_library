import abc


class Expression(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        self._type = "expression"
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
    def check_term(self):
        pass

    @abc.abstractmethod
    def check_vaild(self):
        pass

    def check(self):
        self.check_term()
        self.check_vaild()
        self.standardize()
        pass
