from fraction import Fraction as Frac
from exponents import Exponents as Exps
from integral_expression import IntegralExpression as IE


class quantic_equation:  # 2次方程式クラス
    def __init__(self, a, b, c, d):
        Frac.check(a)
        self.a = a
        Frac.check(b)
        self.b = b
        Frac.check(c)
        self.c = c
        Frac.check(d)
        self.d = d
        self.degree = 2
        quantic_equation.standardize(self)
        self.solution1 = None
        self.solution2 = None

    def set_degree(self):
        if self.a.numerator != 0:
            self.degree = 2
        if self.b.numerator != 0 and self.a.numerator == 0:
            self.degree = 1
        if self.b.numerator == 0 and self.a.numerator == 0:
            self.degree = 0

    def standardize(self):
        self.c = self.c - self.d
        self.d = Frac(0, 1)
        quantic_equation.set_degree(self)

    def get_factor(self):
        return self.a, self.b, self.c, self.d

    def __str__(self):
        return (
            self.a.__str__()
            + "x^2+"
            + self.b.__str__()
            + "x+"
            + self.c.__str__()
            + "="
            + self.d.__str__()
        )

    def show(self):
        print(self)

    @staticmethod
    def solve_zero_degree(equation):
        if equation.c.numerator == 0:
            print("All real numbers are solution")
        else:
            print("No solution")

    @staticmethod
    def solve_liner_equation(equation):
        equation.solution1 = equation.c * Frac(-1, 1) / equation.b
        print("solution is " + equation.solution1.__str__() + " .")

    @staticmethod
    def solve_quadratic_equation(equation):
        fraction = Frac.div(
            Frac.mul(equation.b, Frac(-1, 1)), Frac.mul(equation.a, Frac(2, 1))
        )
        coefficient = Frac.reciprocal(Frac.mul(equation.a, Frac(2, 1)))
        expression = Frac.sub(
            Frac.mul(equation.b, equation.b),
            Frac.mul(Frac.mul(equation.a, equation.c), Frac(4, 1)),
        )
        expressions = Exps(expression, Frac(1, 2))
        equation.solution1 = IE([fraction, expressions])
        equation.solution2 = IE(
            [
                fraction,
                Exps(Frac.mul(Frac(-1, 1), coefficient), expression, Frac(1, 2)),
            ]
        )
        print("solution is ")
        equation.solution1.show()
        equation.solution2.show()

    @staticmethod
    def soulve_equation(equation):
        if equation.degree == 0:
            quantic_equation.solve_zero_degree(equation)
        elif equation.degree == 1:
            quantic_equation.solve_liner_equation(equation)
        elif equation.degree == 2:
            quantic_equation.solve_quadratic_equation(equation)
        else:
            raise ValueError("degree must be 0, 1 or 2")


class quantic_equation_test:
    def __init__(self) -> None:
        pass

    @staticmethod
    def arbitary_test():
        print("input a numerator")
        a_numerator = int(input())
        print("input a denominator")
        a_denominator = int(input())
        print("input b numerator")
        b_numerator = int(input())
        print("input b denominator")
        b_denominator = int(input())
        print("input c numerator")
        c_numerator = int(input())
        print("input c denominator")
        c_denominator = int(input())
        print("input d numerator")
        d_numerator = int(input())
        print("input d denominator")
        d_denominator = int(input())
        e = quantic_equation(
            Frac(a_numerator, a_denominator),
            Frac(b_numerator, b_denominator),
            Frac(c_numerator, c_denominator),
            Frac(d_numerator, d_denominator),
        )
        e.show()
        return e

    @staticmethod
    def random_test():
        e = quantic_equation(
            Frac.random_fraction(),
            Frac.random_fraction(),
            Frac.random_fraction(),
            Frac.random_fraction(),
        )
        e.show()
        return e

    @staticmethod
    def low_degree_test():
        e = quantic_equation_test.arbitary_test()
        e.a = Frac(0, 1)
        e.set_degree()
        e.show()
        quantic_equation.soulve_equation(e)
        e.b = Frac(0, 1)
        e.set_degree()
        e.show()
        quantic_equation.soulve_equation(e)
        e.c = Frac(0, 1)
        e.set_degree()
        e.show()
        quantic_equation.soulve_equation(e)

    @staticmethod
    def quantic_equation_test():
        e = quantic_equation_test.arbitary_test()
        quantic_equation.soulve_equation(e)


quantic_equation_test.low_degree_test()
# quantic_equation_test.quantic_equation_test()
