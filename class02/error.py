def main():
    while True:
        try:
            x= int(input())
            print(x)
        except ValueError:
            print("Please type a number")
        else:
            break

main()
