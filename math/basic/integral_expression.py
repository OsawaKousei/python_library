from exppression import Expression as Exp
from fraction import Fraction as Frac
from exponents import Exponents as Exps


class IntegralExpression(Exp):
    def __init__(self, contents):
        self.contents = contents
        super().__init__()
        self._type = "integral_expression"

    def __str__(self):
        return "integral_expression"

    def standardize(self):
        pass

    def check_term(content):
        if content.type == "fraction":
            return content
        elif content.type == "exponents":
            return content
        elif content.type == "integer":
            return Frac(content, 1)
        else:
            raise TypeError(
                "This term cannot be interpreted as any valid term in an integral expression."
            )

    def check_vaild(self):
        pass
