num = int(input("Enter the number preferred: "))

for row in range(1, num+1):
    for column in range(1, row+1):
        print(column, end=" ")
    for ast in range(num, row, -1):
        print("*", end=" ")
    print(" ")