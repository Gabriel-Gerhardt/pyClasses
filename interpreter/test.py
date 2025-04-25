# test_lexer.py
import pytest
from lexer import Lexer
from token_type import *

def test_next_token():
    input_code = "=+(){},;"
    tests = [
        (ASSIGN, "="),
        (PLUS, "+"),
        (LPAREN, "("),
        (RPAREN, ")"),
        (LBRACE, "{"),
        (RBRACE, "}"),
        (COMMA, ","),
        (SEMICOLON, ";"),
        (EOF, ""),
    ]

    lexer = Lexer(input_code)
    for i, (expected_type, expected_literal) in enumerate(tests):
        tok = lexer.next_token()
        assert tok.type == expected_type, f"tests[{i}] - type wrong: expected={expected_type}, got={tok.type}"
        assert tok.literal == expected_literal, f"tests[{i}] - literal wrong: expected={expected_literal}, got={tok.literal}"
