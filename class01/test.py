def main():
    list =[123,21,32,45,5,433,5632]
    returnBigValue(list)
    print(returnBigValue(list))

def returnBigValue(list):
    big=0
    for i in range (len(list)):

            atual = list[i]

            if atual>big:
                big=atual


    return big

main()
