from expr import *
import string

# tokens
NAME = set(string.ascii_letters + "_")
NUMERIC = set(string.digits + ".")
TERMS = set("+-")
FACTORS = set("*/")
EXPONENT = set("^")
DELIMITERS = set("()")
OPERATORS = TERMS | FACTORS | EXPONENT | DELIMITERS


def read(s):
    return parser(Buffer(lexer(s)))


def lexer(s):
    """Convert an input string into tokens for parsing"""
    tokens = []
    i = 0
    while True:
        if s[i] in NUMERIC:
            token = ""
            while i < len(s) and s[i] in NUMERIC:
                token += s[i]
                i += 1
            try:
                tokens.append(int(token))
            except:
                try:
                    tokens.append(float(token))
                except:
                    raise SyntaxError(f"{token} is not a well-formed number")
        elif s[i] in NAME:
            token = ""
            while i < len(s) and s[i] in NAME:
                token += s[i]
                i += 1
            tokens.append(token)
        elif s[i] in OPERATORS:
            tokens.append(s[i])
            i += 1
        else:
            raise SyntaxError(f"{s[i]} is not a valid token")
        if i == len(s):
            return tokens


def is_literal(token):
    return isinstance(token, int) or isinstance(token, float)


def is_name(token):
    return isinstance(token, str) and token not in OPERATORS


def parser(source):
    """Convert a sequence of tokens into a nested expression"""
    expression = factor(source)
    while source.current in TERMS:
        operator = source.pop()
        right = factor(source)
        expression = BinaryExpr(expression, operator, right)
    return expression


def factor(source):
    expression = exponent(source)
    while source.current in FACTORS:
        operator = source.pop()
        right = exponent(source)
        expression = BinaryExpr(expression, operator, right)
    return expression


def exponent(source):
    expression = call_expr(source)
    while source.current in EXPONENT:
        operator = source.pop()
        right = call_expr(source)
        expression = BinaryExpr(expression, operator, right)
    return expression


def call_expr(source):
    if is_name(source.current) and source.next == "(":  # )
        operator = source.pop()
        right = literal(source)
        return CallExpr(operator, right)
    return literal(source)


def literal(source):
    if is_literal(source.current):
        return Literal(source.pop())
    if is_name(source.current) and source.next != "(":  # )
        return Literal(source.pop())
    elif source.current == "(":  # )
        source.pop()
        expression = parser(source)
        # don't require closing parens but get rid of it if it's there
        if source.current == ")":
            source.pop()
        return expression
    else:
        raise SyntaxError(f"Invalid literal {source.current}")


class Buffer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    @property
    def current(self):
        if self.index >= len(self.tokens):
            return None
        return self.tokens[self.index]

    @property
    def next(self):
        if self.index + 1 >= len(self.tokens):
            return None
        return self.tokens[self.index + 1]

    def pop(self):
        value = self.current
        if self.index < len(self.tokens):
            self.check_implicit_mul()
            self.index += 1
        return value

    def check_implicit_mul(self):
        if is_literal(self.current) or self.current == ")":
            if is_literal(self.next) or is_name(self.next) or self.next == "(":  # )
                self.tokens.insert(self.index + 1, "*")

    def __repr__(self):
        return "Buffer(" + str(self.tokens) + ")"
