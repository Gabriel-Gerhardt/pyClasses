from token_type import *

class Lexer:
    def __init__(self, input: str, position: int = 0, readPosition: int = 0, ch: str = ''):
        self.input = input
        self.position = position
        self.readPosition = readPosition
        self.ch = ch
        self.readChar()

    def readChar(self):
        if self.readPosition >= len(self.input):
            self.ch = '\0'  # EOF
        else:
            self.ch = self.input[self.readPosition]
        self.position = self.readPosition
        self.readPosition += 1

    def nextToken(self):
        self.skipWhitespace()  # Pular espaços em branco antes de processar um token

        next_char = self.ch
        tok: Token

        if next_char == "=":
            if self.peekChar() == ""
           tok = Token(ASSIGN, next_char)
        elif next_char == "+":
           tok = Token(PLUS, next_char)
        elif next_char == "-":
           tok = Token(MINUS, next_char)
        elif next_char == "(":
           tok = Token(LPAREN, next_char)
        elif next_char == ")":
           tok = Token(RPAREN, next_char)
        elif next_char == ",":
           tok = Token(COMMA, next_char)
        elif next_char == "{":
           tok = Token(LBRACE, next_char)
        elif next_char == "}":
           tok = Token(RBRACE, next_char)
        elif next_char == "<":
           tok = Token(LT, next_char)
        elif next_char == ">":
           tok = Token(GT, next_char)
        elif next_char == ".":
           tok = Token(POINT, next_char)
        elif next_char == "/":
           tok = Token(SLASH, next_char)

        elif next_char == "!":
            tok = Token(BANG, next_char)
        elif next_char == "*":
           tok = Token(ASTERISK, next_char)
        elif next_char.isalpha():  # Identificadores começam com letra
           literal = self.readIdentifier()
           tok = self.lookupIdent(literal)
           return tok
        elif next_char.isdigit():  # Tratando números
           literal = self.readNumber()
           tok = Token(GAMOINT, literal)
           return tok
        elif next_char == '\0':
           tok = Token(EOF, "")
        else:
           tok = Token(ILLEGAL, next_char)

        self.readChar()  # Avança para o próximo caractere
        return tok


    def peekChar(self):
        if self.readPosition >= len(self.input):
            return 0
        else:
            return self.input[self.readPosition]


    def skipWhitespace(self):
        while self.ch in " \t\n\r":
            self.readChar()

    def readIdentifier(self):
        pos = self.position
        while self.ch.isalpha() or self.ch.isdigit():
            self.readChar()
        return self.input[pos:self.position]

    def readNumber(self):
        pos = self.position
        while self.ch.isdigit():
            self.readChar()
        return self.input[pos:self.position]

    def lookupIdent(self, ident: str):
        keywords = {
            "gamofunc": GAMOFUNC,
            "gamoreturn": GAMORETURN,
            "gamo": GAMO,
            "real": REAL,
            "barca":BARCA,
            "gamoif":GAMOIF,
            "gamoelse":GAMOELSE,
        }
        if ident in keywords:
            return Token(keywords[ident], ident)
        return Token(IDENT, ident)


    # Look for the next character and give us a expected value
