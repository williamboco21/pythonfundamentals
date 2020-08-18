numbers = [5, 2, 1, 7, 4, 5, 7, 5, 2, 1]
emp = []

# appends an element at the tail or end of the list
# numbers.append(20)

# inserts an element at a given index
# numbers.insert(0, 10)

# removes an element in the list
# numbers.remove(1)

# simply remove all the elements  in the list
# numbers.clear()

# removes the last element of the list
# numbers.pop()

# sort the array
# numbers.sort()

# reverse the list
# numbers.reverse()

# finding the index of an element
# print(numbers.index(5))

# finding the existence of an element
# print(50 in numbers) // numbers = [5, 2, 1, 7, 4, 5, 7, 5, 2, 1]

# counting the occurences of an element or elements
# print(numbers.count(5))

# copies the list
# number2 = numbers.copy()
#
# numbers.append(5)
# print(numbers)
# print(number2)


for number in numbers:
    if number not in emp:
        emp.append(number)

print(numbers)
print(emp)
