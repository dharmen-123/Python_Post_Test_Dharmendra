# Q2. Create an Inheritance program using School System: (3 Marks)
# • Class Person fi walk(), talk()
# • Class Teacher(Person) fi teach()
# • Class Student(Person) fi study()
# Create objects of Teacher and Student, call all methods including inherited ones

class Person:
    def walk(self):
        print("Walk")

    def talk(self):
        print("Talk")

class Teacher(Person):
    def teach(self):
        print("Teach")

class Student(Person):
    def study(self):
        print("Study")

T=Teacher()
T.walk()
T.talk()
T.teach()
print()
S=Student()
S.walk()
S.talk()
S.study()