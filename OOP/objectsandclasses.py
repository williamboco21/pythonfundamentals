class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:

    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False

    def get_average_grade(self):
        ave = 0
        for student in self.students:
            ave += student.get_grade()

        return ave / len(self.students)

    def get_student(self, student):
        for i in self.students:
            if i.name == student.name:
                return student.name



s1 = Student("Liam", 21, 100)
s2 = Student("Juan", 12, 90)
s3 = Student("Emman", 25, 80)

course = Course("Science", 3)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.get_student(s1))
print(course.get_average_grade())
