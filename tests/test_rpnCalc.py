
import pytest
from dataclasses import dataclass

from Algorithm_Calc.rpn_calc import evaluate_rpn
from Algorithm_Calc.shunting_yard import TokenType


@dataclass
class MockToken:
    type: TokenType
    value: str


def test_addition():
    tokens = [
        MockToken(TokenType.NUMBER, "2"),
        MockToken(TokenType.NUMBER, "3"),
        MockToken(TokenType.OPERATOR, "+"),
    ]
    assert evaluate_rpn(tokens) == 5.0


def test_subtraction():
    tokens = [
        MockToken(TokenType.NUMBER, "10"),
        MockToken(TokenType.NUMBER, "4"),
        MockToken(TokenType.OPERATOR, "-"),
    ]
    assert evaluate_rpn(tokens) == 6.0


def test_multiplication():
    tokens = [
        MockToken(TokenType.NUMBER, "2"),
        MockToken(TokenType.NUMBER, "5"),
        MockToken(TokenType.OPERATOR, "*"),
    ]
    assert evaluate_rpn(tokens) == 10.0


def test_division():
    tokens = [
        MockToken(TokenType.NUMBER, "8"),
        MockToken(TokenType.NUMBER, "2"),
        MockToken(TokenType.OPERATOR, "/"),
    ]
    assert evaluate_rpn(tokens) == 4.0


def test_power():
    tokens = [
        MockToken(TokenType.NUMBER, "2"),
        MockToken(TokenType.NUMBER, "3"),
        MockToken(TokenType.OPERATOR, "^"),
    ]
    assert evaluate_rpn(tokens) == 8.0


def test_complex_expression():
    tokens = [
        MockToken(TokenType.NUMBER, "2"),
        MockToken(TokenType.NUMBER, "3"),
        MockToken(TokenType.NUMBER, "4"),
        MockToken(TokenType.OPERATOR, "*"),
        MockToken(TokenType.OPERATOR, "+"),
    ]
    assert evaluate_rpn(tokens) == 14.0


def test_divide_by_zero():
    tokens = [
        MockToken(TokenType.NUMBER, "5"),
        MockToken(TokenType.NUMBER, "0"),
        MockToken(TokenType.OPERATOR, "/"),
    ]
    with pytest.raises(ZeroDivisionError):
        evaluate_rpn(tokens)
