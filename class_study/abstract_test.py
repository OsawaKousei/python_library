import abc


class Field(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def __str__(self):
        pass

    def show(self):
        print(self.name)


class IntField(Field):
    def __init__(self, name, value):
        super().__init__(name)
        self.value = value

    def __str__(self):
        return str(self.value)


def test():
    int_field = IntField("test", 1)
    int_field.show()
    print(int_field)


test()
