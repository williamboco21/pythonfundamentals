def magic(n):
    if n == 1:
        print("Wee")
    else:
        print("Wow", end=" ")
        magic(n-1)


num = int(input("Enter a number greater than 0: "))

while num < 1:
    print("\nNumber must be greater than 0.\n")
    num = int(input("Enter a number greater than 0: "))

magic(num)
