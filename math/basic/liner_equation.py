from exppression import Expression as Exp


class Equation(Exp):
    def __init__(self, content):
        self.content = content
        super().__init__()
        self._type = "equation"

    def __str__(self):
        return "equation"

    def standardize(self):
        pass

    def check_term(self):
        pass

    def check_vaild(self):
        pass
