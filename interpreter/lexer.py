class Lexer:
    def __init__(self,input,position=0,readPosition=0,ch=0):
        self.input= input
        self.position = position
        self.readPosition= readPosition
        self.ch = ch

    def readChar(self):
        if self.readPosition>=len(self.input):
            self.ch=0
        else:
            self.ch = self.input[self.readPosition]
        self.position=self.readPosition
        self.readPosition += 1


def newLexer(input):
    l = Lexer(input)
    l.readChar()
    return l
