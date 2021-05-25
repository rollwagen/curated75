

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        div_sum = 0
        for i in range(1, n+1):
            div, rest = divmod(n, i)
            if rest == 0:
                div_sum += i
        return div_sum


if __name__ == "__main__":
    n = int(input())
    my_calculator = Calculator()
    s = my_calculator.divisorSum(n)
    print("I implemented: " + type(my_calculator).__bases__[0].__name__)
    print(s)
