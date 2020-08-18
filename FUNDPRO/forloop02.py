num = int(input("Enter your preferred number: "))

for row in range(1, num+1):
    for column in range(num, row, -1):
        print("*", end=" ")
    print(" ")