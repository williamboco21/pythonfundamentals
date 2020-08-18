class Mammal:
    def awaw(self):
        print("Nyork")


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


dog = Dog()
dog.awaw()
