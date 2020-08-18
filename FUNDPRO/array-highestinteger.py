numbers = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

higher = numbers[0]
lower = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] > higher:
        higher = numbers[i]
    else:
        if numbers[i] < lower:
            lower = numbers[i]


print(f"\nThe highest number is {higher}.\n"
      f"The lowest number is {lower}.")
