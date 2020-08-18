numbers = [1,2,3,4,5,5,6,6,7,7,8,8,9,9,0]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)