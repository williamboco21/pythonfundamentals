def multiply_by_2(nums):
    for i in range(len(nums)):
        nums[i] *= 2


numbers = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("\nThe contents of the array are: ")
for i in range(len(numbers)):
    print(numbers[i], end=" ")

multiply_by_2(numbers)

print("\n\nThe new contents of the array are: ")
for i in range(len(numbers)):
    print(numbers[i], end=" ")

