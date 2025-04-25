class Token:
    def __init__(self, type_, literal):
        self.type = type_
        self.literal = literal

    def __repr__(self):
        return f"Token(type={self.type}, literal={self.literal})"

ILLEGAL = "ILLEGAL"
EOF     = "EOF"

IDENT = "IDENT"
INT   = "INT"
FLOAT = "FLOAT"

ASSIGN = "="
PLUS   = "+"
MINUS  = "-"

COMMA     = ","
SEMICOLON = ";"
LPAREN    = "("
RPAREN    = ")"
LBRACE    = "{"
RBRACE    = "}"

FUNCTION = "FUNCTION"
LET      = "LET"
