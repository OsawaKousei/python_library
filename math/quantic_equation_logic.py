import fraction_logic as fl


class quantic_equation:
    def __init__(self, a, b, c, d, degree):
        self.a = fl.fraction(a, 1)
        self.b = fl.fraction(b, 1)
        self.c = fl.fraction(c, 1)
        self.d = fl.fraction(d, 1)
        self.degree = degree

    def standerdize_quantic_equation(self):
        if self.a.numerator != 0:
            self.a, self.b, self.c, self.d = self.b, self.c, self.d, 2
        elif self.b.numerator != 0:
            self.b, self.c, self.d = self.c, self.d, 1
        elif self.c.numerator != 0:
            self.c, self.d = self.d, 0
