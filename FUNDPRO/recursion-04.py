def factorial(n):
    if n == 0:
        return 1
    else:
        fact = n * factorial(n-1)
        print(fact)
        return fact


num = int(input("Enter the number you want for factorial: "))

fact = factorial(num)

print(f"\n{num}! is equals to {fact}.")
