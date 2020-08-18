class Length:

    def __init__(self, feet, inches):
        self.__feet = feet
        self.__inches = inches

    @classmethod
    def cons1(cls):
        cls.__feet = float(input("Enter Feet: "))
        cls.__inches = float(input("Enter Inches: "))
        return cls(cls.__feet, cls.__inches)

    def show_length(self):
        print(f"{self.__feet} feet and {self.__inches} inches.")

    def show(self):
        print(self.__feet)
        print(self.__inches)


len1 = Length(11, 6.25)
len2 = Length.cons1()

print("\nLength 1 =", end=' ')
len1.show_length()

print("Length 2 =", end=' ')
len2.show_length()

