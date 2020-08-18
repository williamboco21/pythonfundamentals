class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("Hilaw I am an alien not human.")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color


    def speak(self):
        print("Meow")


    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}.")


class Dog(Pet):

    def speak(self):
        print("Bark")


class Fish(Pet):
    pass


p = Pet("Budoy", 50)
p.speak()
garfield = Cat("Garfield", 7, "Golden Brown")
garfield.speak()
garfield.show()
d = Dog("Fuji", 8)
d.speak()
f = Fish("Nyork", 9)
f.speak()
