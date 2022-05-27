import pytest
import reader as read


def test_lexer():
    assert read.lexer("1+1") == [1, "+", 1]
    assert read.lexer("1.1") == [1.1]
    assert read.lexer("hello-bye") == ["hello", "-", "bye"]
    assert read.lexer("sin(2pi)+1") == ["sin", "(", 2, "pi", ")", "+", 1]
    with pytest.raises(SyntaxError) as e:
        read.lexer("hello goodbye")
    assert "not a valid token" in str(e.value)
    with pytest.raises(SyntaxError) as e:
        read.lexer("1.1.1")
    assert "well-formed number" in str(e.value)


def test_is_literal():
    assert read.is_literal(1) == True
    assert read.is_literal(1.1) == True
    assert read.is_literal("x") == False


def test_is_name():
    assert read.is_name("hello") == True
    assert read.is_name("x") == True
    assert read.is_name("*") == False
    assert read.is_name(3) == False


def test_Buffer():
    b = read.Buffer([1, "+", 1])
    assert b.current == 1
    assert b.pop() == 1
    assert b.current == "+"


@pytest.fixture
def buffer_simple():
    return read.Buffer(read.lexer("1+1"))


def test_literal(buffer_simple):
    l = read.literal(buffer_simple)
    assert isinstance(l, read.Literal)
    assert l.eval() == 1
    with pytest.raises(SyntaxError) as e:
        read.literal(buffer_simple)
    assert "Invalid literal" in str(e.value)


@pytest.fixture
def buffer_call():
    return read.Buffer(read.lexer("sin(2x)"))


@pytest.fixture
def mock_literal(monkeypatch):
    mock = lambda source: read.Literal(source.pop())
    monkeypatch.setattr(read, "literal", mock)


def test_call_expr(buffer_simple, buffer_call, mock_literal):
    c = read.call_expr(buffer_simple)
    assert isinstance(c, read.Literal)
    c = read.call_expr(buffer_call)
    assert isinstance(c, read.CallExpr)
    assert c.operator == "sin"
