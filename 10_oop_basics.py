class Student:
def init(self, name, major, gpa):
self.name = name
self.major = major
self.gpa = gpa
def display_info(self):
    print("Name:", self.name)
    print("Major:", self.major)
    print("GPA:", self.gpa)
student1 = Student(“Amjad”, “Computer Science”, 3.60)
student1.display_info()
