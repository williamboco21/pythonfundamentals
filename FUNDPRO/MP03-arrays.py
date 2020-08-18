def get_numbers(nums):
    for i in range(10):
        num = int(input(f"Enter integer {i + 1}: "))
        nums.append(num)


def add_numbers(num, total):
    for i in range(len(numbers)):
        if 5 <= num[i] <= 10:
            total += num[i]

    return total


numbers = []
sum_of_numbers = 0

get_numbers(numbers)

result = add_numbers(numbers, sum_of_numbers)

print(f"\nThe sum of numbers between 5 and 10 is {result}.")
