numbers = []
sum_of_numbers = 0

for i in range(10):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

for i in range(len(numbers)):
    if 5 <= numbers[i] <= 10:
        sum_of_numbers += numbers[i]

print(f"\nThe sum of numbers between 5 and 10 is {sum_of_numbers}.")
