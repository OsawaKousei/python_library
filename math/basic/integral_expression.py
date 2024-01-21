from exppression import Expression as Exp
from exppression import Operator as Op
from fraction import Fraction as Frac
from exponents import Exponents as Exps
from integer import Integer as Intg


class IntegralExpression(Exp):
    def __init__(self):
        super().__init__()
        self._type = "integral_expression"

    def __str__(self):
        res = ""
        for i in self.cont.inorder():
            res += str(i)
        return res

    def standardize(self):
        pass

    def term_check(content):
        if not hasattr(content, "type"):
            raise TypeError(
                "This variable has no attribute 'type' and cannot be interpreted as an integral expression."
            )
        if content.type == "fraction":
            return content
        elif content.type == "exponents":
            return content
        elif content.type == "integer":
            return Frac(content, 1)
        elif content.type == "operator":
            return content
        else:
            raise TypeError(
                "This variable has an illegal type that cannot be interpreted as an integral expression. type:"
                + str(content.type)
            )

    def check(self):
        if not hasattr(self, "cont"):
            raise AttributeError("This integral expression has no attribute 'cont'.")
        for i in self.cont.inorder():
            IntegralExpression.term_check(i)
        return self


class IntegralExpression_test:
    def __init__(self) -> None:
        pass

    def test_expression(self):
        t = IntegralExpression()
        t.cont.set_root(Op("+"))
        print(t.cont.get_root())
        t.cont.insert_left(Frac(1, 2))
        t.cont.insert_right(Exps(Frac(2, 3), Frac(1, 2)))
        print(t)


# sIntegralExpression_test().test_expression()
