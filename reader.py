from expr import *
import string

# tokens
NAME_STARTS = set(string.ascii_letters)
NAME_INNERS = NAME_STARTS | set(string.digits)
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
        elif s[i] in NAME_STARTS:
            token = ""
            while i < len(s) and s[i] in NAME_INNERS:
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


def parser(source, expr):
    """Convert a sequence of tokens into a nested expression"""
    val = source.pop()
    if is_literal(val):
        return term(source, val)


class Buffer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    @property
    def current(self):
        return self.tokens[self.index]

    def pop(self):
        value = self.current()
        self.index += 1
        return value
