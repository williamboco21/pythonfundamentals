sum = 0
average = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    average.append(num)
    sum += num

average = float(sum) / 5
print(f"\nThe average of the quizzes is {average}.")
