def count(n):
    if n == 1:
        print("\nThe numbers are: \n")
        print("1", end=" ")
    else:
        count(n-1)
        print(n, end=" ")


num = int(input("Enter the value of n: "))

count(num)
