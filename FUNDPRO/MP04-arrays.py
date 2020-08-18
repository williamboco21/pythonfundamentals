def get_numbers(nums):
    numbers_to_enter = int(input(f"Please enter the numbers to be entered: "))
    print()

    for i in range(numbers_to_enter):
        num = int(input(f"Enter integer {i + 1}: "))
        nums.append(num)


def add_numbers(nums, sum_of_numbers):
    for i in range(len(nums)):
        if 5 <= nums[i] <= 10:
            sum_of_numbers += nums[i]

    return sum_of_numbers
numbers = []
sum_of_numbers = 0

get_numbers(numbers)

total = add_numbers(numbers, sum_of_numbers)

print(f"\nThe sum of numbers between 5 and 10 is {total}.")
