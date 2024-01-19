class basic:
    def __init__(self):
        self.type = "basic"

    @staticmethod
    def check(variable):
        if not hasattr(variable, "type"):
            raise TypeError("this variable has no type. this variable can't be read")
        return variable.type
