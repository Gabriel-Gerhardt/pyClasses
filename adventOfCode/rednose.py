def main():
    sum=0

    newLine=[]
    with open('data/rednose.txt','r') as file:
        for line in file:
            newLine = changeToNumber(line)
            sum+= calculaRisco(newLine)
            print(sum,"-",newLine)
    print(sum)



def calculaRisco(line):
    flag = False
    flag2 = False
    for i in range(len(line)-1):
        if line[i]> line[i+1]:
            flag=True

        if line[i]<line[i+1]:
            flag2=True

        if line[i]>line[i+1]+3:
            return 0

        if line[i]+3<line[i+1]:
            return 0

        if line[i]== line[i+1]:
            return 0
        if flag==True and flag2==True:
            return 0

    return 1

def calculaRiscoComDampener(line):
    if calculaRisco(line[:]) == 1:
        return 1

    for i in range(len(line)):
        new_line = line[:i] + line[i+1:]
        if calculaRisco(new_line) == 1:
            return 1

    return 0

def changeToNumber(line):
    args= line.split(" ")
    newLine= []
    for i in range(len(args)):
        if i!=len(args):
            newLine.append(int(args[i]))

    return newLine

main()
