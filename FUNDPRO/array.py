quiz_score = []

for i in range(5):
    num = int(input(f"Enter score for quiz {i+1}: "))
    quiz_score.append(num)

count = 0
for i in quiz_score:
    print(f"\nThe score for quiz {count+1} is {i}.")
    count += 1


