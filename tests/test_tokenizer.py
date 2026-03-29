from Algorithm_Calc.shunting_yard import tokenizeExpression, TokenType

def test_Tokenize_simple_expression():
    tokens = tokenizeExpression("2+3")

    assert len(tokens) == 3

    assert tokens[0].value == "2"
    assert tokens[0].type == TokenType.NUMBER

    assert tokens[1].value == '+'
    assert tokens[1].type == TokenType.OPERATOR

    assert tokens[2].value == "3"
    assert tokens[2].type == TokenType.NUMBER


def test_tokenize_parentheses():
    tokens = tokenizeExpression("(2 + 3)")

    values = [t.value for t in tokens]
    types = [t.type for t in tokens]

    assert values == ["(", "2", "+", "3", ")"]
    assert types == [
        TokenType.PARENTHESES,
        TokenType.NUMBER,
        TokenType.OPERATOR,
        TokenType.NUMBER,
        TokenType.PARENTHESES,
    ]

def test_multiple_digit_number():
    tokens = tokenizeExpression("12 + 3")

    assert tokens[0].value == "12"
    assert tokens[0].type == TokenType.NUMBER

    
def test_float_number():
    tokens = tokenizeExpression("3.5 * 2")

    assert tokens[0].value == "3.5"
    assert tokens[0].type == TokenType.NUMBER


