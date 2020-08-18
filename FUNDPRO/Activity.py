def is_sorted(myList):
    anotherList = myList[:]
    anotherList.sort()
    if myList == anotherList:
        return True
    else:
        return False

numberList = [18, 19, 20, 21]
letterList = ['c', 'a', 'b', 'e']

print(is_sorted(numberList))
print(is_sorted(letterList))