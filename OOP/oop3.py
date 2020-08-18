class Counter:

    def __init__(self, count=0):
        self.__count = count
        print("Executing Constructor!")

    def inc_count(self):
        self.__count += 1

    def get_count(self):
        return self.__count


count1 = Counter()
count2 = Counter(5)
print(count1.get_count())
print(count2.get_count())


