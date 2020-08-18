number = [100, 500, 1000, 2000, 5, 6, 7, 8, 4, 67]
max_num = number[0]

for i in number:
    if max_num < i:
        max_num = i

print(f"The highest value is {max_num}.")
