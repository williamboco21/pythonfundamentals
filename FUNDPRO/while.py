counter = 0
sum_of_numbers = 0

while counter < 5:
    number = int(input("Enter a number: "))
    sum_of_numbers += number
    counter += 1

print(f'\nThe sum is {sum_of_numbers}.')
