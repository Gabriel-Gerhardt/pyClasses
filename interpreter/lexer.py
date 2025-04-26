from token_type import *



class Lexer:
    def __init__(self,input,position:int=0,readPosition:int=0,ch=0):
        self.input= input
        self.position = position
        self.readPosition= readPosition
        self.ch = ch
        self.readChar()


    def readChar(self):
        if self.readPosition>=len(self.input):
            self.ch=0
        else:
            self.ch = self.input[self.readPosition]
        self.position=self.readPosition
        self.readPosition += 1

    def nextToken(self):
        tok: Token
        next_byte= self.ch


        if next_byte == "=":
            tok = Token(ASSIGN,self.ch)

        elif next_byte == "+":
            tok = Token(PLUS,self.ch)

        elif next_byte == ";":
            tok = Token(SEMICOLON,self.ch)


        elif next_byte == "(":
            tok = Token(LPAREN,self.ch)

        elif next_byte == ")":
            tok = Token(RPAREN,self.ch)

        elif next_byte == ",":
            tok = Token(COMMA,self.ch)

        elif next_byte == "{":
            tok = Token(LBRACE,self.ch)

        elif next_byte == "}":
            tok = Token(RBRACE,self.ch)
        else:
            tok = Token(EOF, "")

        self.readChar()
        return tok

def newLexer(input):
    l = Lexer(input)
    l.readChar()
    return l
