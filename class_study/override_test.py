import abc


class Parent:
    def __init__(self):
        self.check()

    @abc.abstractmethod
    def check(self):
        pass


class child(Parent):
    def __init__(self, value):
        self.value = value
        self.check()

    def check(self):
        if type(self.value) != int:
            raise TypeError("value is not an integer")
        print(self.value)


class child2(Parent):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.check()

    def check(self):
        if type(self.value) != int:
            raise TypeError("value is not an integer")
        print(self.value)


class child3(Parent):
    def __init__(self, value):
        self.value = value  # 先にvalueを定義しておく
        super().__init__()

    def check(self):
        if type(self.value) != int:
            raise TypeError("value is not an integer")
        print(self.value)


def main():
    a = child(1)

    # b = child2(2) ←エラーになる

    c = child3(3)  # ←エラーにならない


main()
