class Test:
    def __init__(self, name):
        self.name = name

    # 以下のようにMethodを定義することで、
    def show(self):
        if not hasattr(self, "name"):
            self = Test(self)
        print(self.name)


def test():
    Test.show("test")
    t = Test("test")
    t.show()


test()
