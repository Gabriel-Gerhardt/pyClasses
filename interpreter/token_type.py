class Token:
    def __init__(self, type, literal):
        self.type = type
        self.literal = literal

    def __repr__(self):
        return f"Token(type={self.type}, literal={self.literal})"

ILLEGAL = "ILLEGAL"
EOF     = "EOF"

IDENT = "IDENT"
GAMOINT   = "INT"
GAMOFLOAT = "FLOAT"

ASSIGN = "="
PLUS = "+"
MINUS = "-"
BANG = "!"
ASTERISK = "*"
SLASH = "/"
LT = "<"
GT = ">"
POINT ="."

COMMA     = ","
LPAREN    = "("
RPAREN    = ")"
LBRACE    = "{"
RBRACE    = "}"

GAMOFUNC = "FUNCTION"
GAMO      = "LET"
GAMORETURN   ="RETURN"
REAL = "TRUE"
BARCA= "FALSE"
GAMOIF ="IF"
GAMOELSE = "ELSE"
EQ = "=="
NOT_EQ= "!="
