# organize two lists,
# Pair up the smallest number in the left list with the smallest number in the right list
# then the second-smallest left number with the second-smallest right number, and so on.
# Within each pair, figure out how far apart the two numbers are;
# you'll need to add up all of those distances.
# For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4
# if you pair up a 9 with a 3, the distance apart is 6.
import copy


def main():
    list1 = []
    list2 = []
    with open('data/histeria.txt','r') as file:
        for line in file:
            args= line.split("  ")
            list1.append(int(args[0]))
            list2.append(int(args[1]))


    list1.sort()
    list2.sort()
    distance = calculateDistance(list1,list2)
    value1 = similarity(list1,list2)
    print(distance)
    print(value1)


def calculateDistance(l1, l2):
    sum = 0
    distance=0
    for i in range(len(l1)):
        if l1[i]>l2[i]:
            distance = l1[i]-l2[i]
            sum +=distance

        if l2[i]> l1[i]:
            distance = l2[i]-l1[i]
            sum +=distance

    return sum



def similarity(l1,l2):
    cont=0
    clone =l1.copy()
    finalValue=0
    for x in l1:
        clone[cont]=0
        for y in l2:
            if x==y:

                clone[cont]+=1

        cont +=1


    for i in range(len(clone)):
        finalValue += l1[i]*clone[i]

    return finalValue


main()
