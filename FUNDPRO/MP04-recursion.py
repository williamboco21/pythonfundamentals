def asterisk(n):
    if n == 1:
        print("*", end=" ")
    else:
        asterisk(n-1)
        print("")
        for i in range(n):
            print("*", end=" ")

num = int(input("Enter the value of number: "))
asterisk(num)
