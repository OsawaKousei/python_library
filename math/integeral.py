class integeral:
    def __init__():
        pass

    @staticmethod
    def gcd(a, b):
        while b:  # while文では0以外の値はTrueとして扱われる
            a, b = b, a % b
        return a

    @staticmethod
    def lcm(a, b):
        return a * b // integeral.gcd(a, b)  # //は整数除算

    @staticmethod
    def natural_num_power(base, exponent):
        if not (type(base) == int) or not (type(exponent) == int):
            raise TypeError(
                "base and exponent must be natural numbers in this function: integeral_power"
            )
        if base <= 0 or exponent <= 0:
            raise ValueError(
                "base and exponent must be natural numbers in this function: integeral_power"
            )
        res = base
        if exponent > 0:
            for i in range(exponent - 1):
                res *= base
        return res

    @staticmethod
    def max_exponential_divide(base, exponent):  # bese=p^exponentを満たす最大のpを返す
        p = 1
        q = 1
        while integeral.natural_num_power(p, exponent) <= base:
            if base % integeral.natural_num_power(p, exponent) == 0:
                q = p
            p += 1

        return q


class integeral_test:
    def __init__(self):
        pass

    def max_exponential_divide_test():
        print("input base")
        base = int(input())
        print("input exponent")
        exponent = int(input())
        print(integeral.max_exponential_divide(base, exponent))
