class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello there! My name is {self.name}. Nice to meet you!")


john = Person("John Smith")
john.talk()

bob = Person("Bob Marley")
bob.talk()
