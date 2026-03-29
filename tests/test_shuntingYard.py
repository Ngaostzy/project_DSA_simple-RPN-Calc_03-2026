
from Algorithm_Calc.shunting_yard import tokenizeExpression, shuntingYard


def test_simple_expression():
    tokens = tokenizeExpression("2 + 3")
    rpn = shuntingYard(tokens)

    values = [t.value for t in rpn]
    assert values == ["2", "3", "+"]


def test_operator_precedence():
    tokens = tokenizeExpression("2 + 3 * 4")
    rpn = shuntingYard(tokens)

    values = [t.value for t in rpn]
    assert values == ["2", "3", "4", "*", "+"]


def test_parentheses():
    tokens = tokenizeExpression("(2 + 3) * 4")
    rpn = shuntingYard(tokens)

    values = [t.value for t in rpn]
    assert values == ["2", "3", "+", "4", "*"]


def test_right_associative_power():
    tokens = tokenizeExpression("2 ^ 3 ^ 2")
    rpn = shuntingYard(tokens)

    values = [t.value for t in rpn]
    assert values == ["2", "3", "2", "^", "^"]
