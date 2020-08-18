average = 0
count = 0
list_num = []

while count < 5:
    num = int(input(f"Enter score for quiz {count+1}: "))
    list_num.append(num)
    average += num
    count += 1

print()
count = 0
while count < 5:
    print(f"The score of quiz {count+1} is {list_num[count]}.")
    count += 1


