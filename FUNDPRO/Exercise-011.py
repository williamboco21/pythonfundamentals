num = int(input(""))

if (2 <= num <= 5) and num % 2 == 0:
    print("Not Weird")
elif (6 <= num <= 20) and num % 2 == 0:
    print("Weird")
elif num > 20 and num % 2 == 0:
    print("Not Weird")
else:
    print("Weird")