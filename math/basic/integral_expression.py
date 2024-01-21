from exppression import Expression as Exp
from fraction import Fraction as Frac
from exponents import Exponents as Exps


class IntegralExpression(Exp):
    def __init__(self):
        super().__init__()
        self._type = "integral_expression"

    def __str__(self):
        return "integral_expression"

    def standardize(self):
        pass

    def term_check(content):
        if not hasattr(content, "type"):
            raise TypeError(
                "This variable has no attribute 'type' and cannot be interpreted as an integral expression."
            )
        if content.cont.type == "fraction":
            return content
        elif content.type == "exponents":
            return content
        elif content.type == "integer":
            return Frac(content, 1)
        else:
            raise TypeError(
                "This variable has an illegal type that cannot be interpreted as an integral expression. type:"
                + str(content.type)
            )

    def check(self):
        if not hasattr(self, "cont"):
            raise AttributeError("This integral expression has no attribute 'cont'.")


class IntegralExpression_test:
    def __init__(self) -> None:
        pass

    def test_expression(self):
        t = IntegralExpression()
        t.cont.set_root(Exps(2, 3))
        t.cont.insert_left(Frac(1, 2))
        t.cont.insert_right(Frac(1, 3))
        t.cont.inorder()


IntegralExpression_test().test_expression()
