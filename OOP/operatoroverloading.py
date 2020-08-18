class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self):
        return f"{self.full_name()} - {self.email}"

    def __add__(self, other_self):
        return self.pay + other_self.pay

    def __len__(self):
        return len(self.full_name())


emp1 = Employee("William", "Boco", 25000)
emp2 = Employee("Chuchoy", "Katsu", 15000)

print(emp1)
print(emp1 + emp2)
print(len(emp1))
