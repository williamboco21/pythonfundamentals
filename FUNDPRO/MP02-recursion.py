def addition(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        sum = n + addition(n-1)
        return sum


num = int(input("Enter the value of n: "))

total = addition(num)

print(f"\nThe sum is {total}")
