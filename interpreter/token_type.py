class Token:
    def __init__(self, type_, literal):
        self.type = type_
        self.literal = literal

    def __repr__(self):
        return f"Token(type={self.type}, literal={self.literal})"

ILLEGAL = "ILLEGAL"
EOF     = "EOF"

IDENT = "IDENT"
GAMOINT   = "INT"
GAMOFLOAT = "FLOAT"

ASSIGN = "="
PLUS   = "+"
MINUS  = "-"

COMMA     = ","
SEMICOLON = ";"
LPAREN    = "("
RPAREN    = ")"
LBRACE    = "{"
RBRACE    = "}"

GAMOFUNC = "FUNCTION"
GAMO      = "LET"
GAMORETURN   ="RETURN"
