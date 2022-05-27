def simplify(val):
    if isinstance(val, float) and val == int(val):
        val = int(val)
    return val


class Expression:
    def __init__(self, *args):
        self.args = args

    def eval(self):
        raise NotImplementedError

    def __repr__(self):
        arguments = "(" + ", ".join([repr(arg) for arg in self.args]) + ")"
        return type(self).__name__ + arguments


class BinaryExpr(Expression):
    def __init__(self, left, operator, right):
        Expression.__init__(self, left, operator, right)
        self.left = left
        self.operator = operator
        self.right = right

    def eval(self):
        return simplify(GLOBALS[self.operator](self.left.eval(), self.right.eval()))


class CallExpr(Expression):
    def __init__(self, operator, operand):
        Expression.__init__(self, operator, operand)
        self.operator = operator
        self.operand = operand

    def eval(self):
        return simplify(GLOBALS[self.operator](self.operand.eval()))


class Literal(Expression):
    def __init__(self, value):
        Expression.__init__(self, value)
        self.value = value

    def eval(self):
        if isinstance(self.value, int) or isinstance(self.value, float):
            return simplify(self.value)
        else:
            return GLOBALS[self.value]


from operator import add, sub, mul, truediv
from math import log, sqrt, pi, e

GLOBALS = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv,
    "^": pow,
    "log": log,
    "sqrt": sqrt,
    "neg": lambda x: -x,
    "pi": pi,
    "e": e,
}
