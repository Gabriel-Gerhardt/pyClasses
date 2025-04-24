def main():
    students = ["john","pork"]
    cont(students)

def cont(x):
    for names in x:
        print(names)
    for i in range(len(x)):
        print(x[i])
main()
