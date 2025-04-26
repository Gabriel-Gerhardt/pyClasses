# test_lexer.py
import pytest
from lexer import Lexer
from token_type import *
import os

def test_next_token():
    path = os.path.join(os.path.dirname(__file__), "GAMO.txt")
    with open(path, "r") as arquivo:
        input_code = arquivo.read()

    tests = [
            (GAMOFUNC, "gamofunc"),
            (IDENT, "add"),
            (LPAREN, "("),
            (RPAREN, ")"),
            (LBRACE, "{"),
            (GAMO, "gamo"),
            (IDENT, "y"),
            (ASSIGN, "="),
            (GAMOINT, "2"),
            (GAMO, "gamo"),
            (IDENT, "x"),
            (ASSIGN, "="),
            (GAMOINT, "10"),
            (GAMORETURN, "gamoreturn"),
            (IDENT, "x"),
            (PLUS, "+"),
            (IDENT, "y"),
            (RBRACE, "}"),
        ]

    lexer = Lexer(input_code)

    for i, (expected_type, expected_literal) in enumerate(tests):
        tok = lexer.nextToken()
        assert tok.type == expected_type, f"tests[{i}] - type wrong: expected={expected_type}, got={tok.type}"
        assert tok.literal == expected_literal, f"tests[{i}] - literal wrong: expected={expected_literal}, got={tok.literal}"
