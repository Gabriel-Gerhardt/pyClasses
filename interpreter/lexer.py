class Lexer:
    def __init__(self,input,position=0,readPosition=0,ch=0):
        self.input= input
        self.position = position
        self.readPosition= readPosition
        self.ch = ch

def newLexer(input):
    l = Lexer(input)
    return l
