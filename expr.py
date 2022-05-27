class Expression:
    def __init__(self, *args):
        self.args = args

    def eval(self):
        raise NotImplementedError

    def __repr__(self):
        arguments = "(" + ", ".join([str(arg) for arg in self.args]) + ")"
        return type(self).__name__ + arguments


class BinaryExpr(Expression):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def eval(self):
        return GLOBALS[self.operator](self.left, self.right)


class UnaryExpr(Expression):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def eval(self):
        return GLOBALS[self.operator](self.operand)


class Literal(Expression):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value


from operator import add, sub, mul, truediv
from math import log, sqrt

GLOBALS = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": truediv,
    "pow": pow,
    "log": log,
    "sqrt": sqrt,
    "neg": lambda x: -x,
}
