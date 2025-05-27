
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

#Student Subclass
class Student(Person):
    def __init__(self, name, age, email, student_id, course):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.course = course

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")

#Lecturer Subclass
class Lecturer(Person):
    def __init__(self, name, age, email, staff_id, department):
        super().__init__(name, age, email)
        self.staff_id = staff_id
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Staff ID: {self.staff_id}")
        print(f"Department: {self.department}")

#Staff Subclass
class Staff(Person):
    def __init__(self, name, age, email, role):
        super().__init__(name, age, email)
        self.role = role

    def display_info(self):
        super().display_info()
        print(f"Role: {self.role}")


print("___ STUDENT INFO ___")
student = Student("Kevin", 20, "kevin@student.univ.edu", "B23394", "Software Engineering")
student.display_info()

print("\n___ LECTURER INFO ___")
lecturer = Lecturer("Dr. John", 45, "john@univ.edu", "L5678", "Engineering")
lecturer.display_info()

print("\n___ STAFF INFO ___")
staff = Staff("Mrs. Jane", 35, "jane@univ.edu", "Dean")
staff.display_info()