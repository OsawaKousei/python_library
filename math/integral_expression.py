from basic import basic
from fraction import fraction as fl
from simple_exponents import simple_exponents as ex


class integeral_expression:  # 整式クラス
    def __init__(self, expression):
        self.type = "integeral_expression"
        self.expression = expression
        self.check()

    def check(self):
        if not basic.check(self) == "integeral_expression":
            raise TypeError("this variable is not integeral_expression")

    @staticmethod
    def get_term_string(term):
        basic.check(term)
        if term.type == "fraction":
            return fl.get_string(term)
        elif term.type == "exponents":
            return ex.get_string(term)

    @staticmethod
    def get_string(expression):
        integeral_expression.check(expression)
        if expression.type == "integeral_expression":
            string = ""
            for term in expression.expression:
                string += integeral_expression.get_term_string(term)
            return string
        else:
            raise TypeError("this variable is not integeral_expression")


class integeral_expression_test:
    def __init__(self):
        pass

    @staticmethod
    def sample_test():
        a = integeral_expression([fl(1, 1), ex(fl(1, 1), fl(1, 1))])
        print(integeral_expression.get_string(a))


integeral_expression_test.sample_test()
