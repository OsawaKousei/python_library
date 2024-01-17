class test_class:
    def __init__(self, v1, v2):
        self.name = "test_class"
        self.v1 = v1
        self.v2 = v2

    def print_name(self):
        print(self.name)

    def get_value(self):
        return self.v1, self.v2

    @staticmethod
    def add(fraction):
        return fraction[0] + fraction[1]


def test_class_test():
    test = test_class(1, 2)
    test.print_name()
    print(test.get_value())
    print(test_class.add(test.get_value()))
    print(hasattr(test, "name"))
    print(hasattr(test, "v3"))
    raise Exception("test")


test_class_test()
