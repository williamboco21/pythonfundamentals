num = int(input("Enter a positive integer: "))
count = 0
add = 0

while num >= 0:
    count += 1
    add += num
    num = int(input("Enter a positive integer: "))

average = add / count

print(f"\nThe average is {average}.")
