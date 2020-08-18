MAX = 100


def get_number(numbers, num):
    print()

    for i in range(num):
        num_ber = int(input(f"Enter integer {i+1}: "))
        numbers.append(num_ber)


def highest_number(numbers):
    highest = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] > highest:
            highest = numbers[i]

    print(f"\nThe highest number is {highest}.\n")

    return highest


def indices(numbers, high):
    highest = high

    print("The indices are: ")
    for i, val in enumerate(numbers):
        val = highest
        if numbers[i] == val:
            print(i, end=" ")


numbers = []
num = int(input("How many numbers do you want to enter? "))

while num <= 0 or num > MAX:
    print("\nPlease enter a number between 1 and 100.\n")
    num = int(input("How many numbers do you want to enter? "))

get_number(numbers, num)
high = highest_number(numbers)
indices(numbers, high)

