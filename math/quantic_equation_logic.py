from fraction import fraction as fl


class quantic_equation:
    def __init__(self, a, b, c, d):
        fl.check(a)
        self.a = a
        fl.check(b)
        self.b = b
        fl.check(c)
        self.c = c
        fl.check(d)
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
        self.c = fl.sub(self.c, self.d)
        self.d = fl(0, 1)
        quantic_equation.set_degree(self)

    def get_factor(self):
        return self.a, self.b, self.c, self.d

    def get_string(self):
        return (
            fl.get_string(self.a)
            + "x^2+"
            + fl.get_string(self.b)
            + "x+"
            + fl.get_string(self.c)
            + "="
            + fl.get_string(self.d)
        )

    def show(self):
        print(self.get_string())

    @staticmethod
    def solve_zero_degree(equation):
        if equation.c.numerator == 0:
            print("All real numbers are solution")
        else:
            print("No solution")

    @staticmethod
    def solve_liner_equation(equation):
        equation.solution1 = fl.div(fl.mul(equation.c, fl(-1, 1)), equation.b)
        print("solution is " + fl.get_string(equation.solution1))

    @staticmethod
    def soulve_equation(equation):
        if equation.degree == 0:
            quantic_equation.solve_zero_degree(equation)
        elif equation.degree == 1:
            quantic_equation.solve_liner_equation(equation)
        elif equation.degree == 2:
            pass
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
            fl(a_numerator, a_denominator),
            fl(b_numerator, b_denominator),
            fl(c_numerator, c_denominator),
            fl(d_numerator, d_denominator),
        )
        e.show()
        return e

    @staticmethod
    def random_test():
        e = quantic_equation(
            fl.random_fraction(),
            fl.random_fraction(),
            fl.random_fraction(),
            fl.random_fraction(),
        )
        e.show()
        return e

    @staticmethod
    def low_degree_test():
        e = quantic_equation_test.arbitary_test()
        e.a = fl(0, 1)
        e.set_degree()
        e.show()
        quantic_equation.soulve_equation(e)
        e.b = fl(0, 1)
        e.set_degree()
        e.show()
        quantic_equation.soulve_equation(e)
        e.c = fl(0, 1)
        e.set_degree()
        e.show()
        quantic_equation.soulve_equation(e)


quantic_equation_test.low_degree_test()
