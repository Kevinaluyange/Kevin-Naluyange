import json
import os
from collections import Counter

# Student Information 
STUDENT_NAME = "john doe"
STUDENT_NUMBER = "123"
REGISTRATION_NUMBER = "AB1234"

class Student:
    def __init__(self, admin_no, name):
        """Initialize a student with admin number, name and optionally marks."""
        self.admin_no = admin_no
        self.name = name
        self.marks = {
            'Math': None,
            'Science': None,
            'SST': None,
            'English': None
        }

    def set_marks(self, subject, marks):
        """Set marks for a specific subject. Possible subjects  are Maths, SST, English, and Science."""
        try:
            marks = int(marks)
            if 0 <= marks <= 100 and subject in self.marks:
                self.marks[subject] = marks
                return True
            return False
        except ValueError:
            return False

    def get_marks(self, subject):
        """Return student's mark for the specific subject. The returned mark should be between an Integer between 0 and 100 or none if not available"""
        return self.marks.get(subject)

    def edit_marks(self, subject, new_marks):
        """Edit marks for a specific subject."""
        return self.set_marks(subject, new_marks)

    def to_dict(self):
        """Convert student object to dictionary format for easier storage."""
        return {
            'admin_no': self.admin_no,
            'name': self.name,
            'marks': self.marks
        }

    @classmethod
    def from_dict(cls, data):
        """Create student object from dictionary."""
        student = cls(data['admin_no'], data['name'])
        student.marks = data['marks']
        return student

class Gradebook:
    def __init__(self, filename='gradebook_data.txt'):
        """Initialize an empty gradebook. Load existing data if available."""
        self.filename = filename
        self.students = {}
        self.load_data()

    def save_data(self):
        """Save gradebook data to a file in JSON format"""
        data = {
            admin_no: student.to_dict() 
            for admin_no, student in self.students.items()
        }
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        """Loads gradebook data from an existing readable file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    self.students = {
                        admin_no: Student.from_dict(student_data)
                        for admin_no, student_data in data.items()
                    }
            except json.JSONDecodeError:
                self.students = {}

    def add_student(self, student):
        """Add a student to the gradebook and save the data afterward"""
        if student.admin_no not in self.students:
            self.students[student.admin_no] = student
            self.save_data()
            return True
        return False

    def get_student(self, admin_no):
        """This should return a student using admin_no. or None if the student is not found"""
        if admin_no in self.students:
            return self.students.get(admin_no)

    def delete_student(self, admin_no):
        """Delete a student from the gradebook using their admin number."""
        if admin_no in self.students:
            del self.students[admin_no]
            self.save_data()
            return True
        return False

    def get_subject_stats(self, subject):
        """Calculate statistics for a specific subject."""
        marks = [
            student.marks[subject] 
            for student in self.students.values() 
            if student.marks[subject] is not None
        ]
        
        if not marks:
            return None
            
        mode_data = Counter(marks)
        mode_mark = max(mode_data, key=mode_data.get)
        
        return {
            f'Average_{subject}': sum(marks) / len(marks),
            f'Max_{subject}': max(marks),
            f'Min_{subject}': min(marks),
            f'Mode_{subject}': mode_mark,
            f'Mode_Freq_{subject}': mode_data[mode_mark]
        }

    def view_statistics(self):
        """Display statistics about the all subjects"""
        subjects = ['Math', 'Science', 'SST', 'English']
        stats = {}
        
        for subject in subjects:
            subject_stats = self.get_subject_stats(subject)
            if subject_stats:
                stats.update(subject_stats)
            else:
                stats.update({
                    f'Average_{subject}': 'No data',
                    f'Max_{subject}': 'No data',
                    f'Min_{subject}': 'No data',
                    f'Mode_{subject}': 'No data',
                    f'Mode_Freq_{subject}': 'No data'
                })
        
        return stats

    def view_student_grades(self, admin_no):
        """returns grades of a specific student."""
        student = self.get_student(admin_no)
        if student:
            return student.marks
        return None

    def print_gradebook(self):
        """Return gradebook details including total number of students"""
        return {
            'total_students': len(self.students),
            'student_details': {
                student.admin_no: student.name 
                for student in self.students.values()
            }
        }

def print_menu():
    """Print the menu for user interaction. Do not change this"""
    print("--------------------Menu--------------------")
    print("1 - Add student")
    print("2 - Delete student, given an admin_no")
    print("3 - View statistics about the grades")
    print("4 - View student grades")
    print("5 - Edit student grades")
    print("6 - Print Gradebook")
    print("m - Print menu")
    print("c - Clear Screen")
    print("q - Quit system\n")

def main():
    """Main function to run the gradebook application."""
    
    gradebook = Gradebook()
    while True:
        print_menu()
        choice = input("Select an option: ").strip().lower()
        #Be sure to validate any values entered by user and act accordingly 
        if choice == '1':
            admin_no = input("Enter admin number: ").strip()
            if not admin_no:
                print("Admin number cannot be empty.")
                continue
                
            name = input("Enter student name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
                
            student = Student(admin_no, name) ##creates a new student object with provided admin_no and name
            
            for subject in ['Math', 'Science', 'SST', 'English']:
                while True:
                    try:
                        marks = int(input(f"Enter {subject} marks (0-100): "))
                        if 0 <= marks <= 100:
                            student.set_marks(subject, marks)
                            break
                        print("Marks must be between 0 and 100.")
                    except ValueError:
                        print("Please enter a valid number.")
            
            if gradebook.add_student(student): ##adds new student to gradebook 
                print(f"Student {name} added successfully.")
            else:
                print("Student with this admin number already exists.")

        elif choice == '2':
            admin_no = input("Enter admin number to delete: ").strip()
            if gradebook.delete_student(admin_no):
                print(f"Student with admin number {admin_no} deleted successfully.")
            else:
                print("Student not found.")

        elif choice == '3':
            stats = gradebook.view_statistics()
            print("\nGrade Statistics:")
            for key, value in stats.items():
                print(f"{key}: {value}")

        elif choice == '4':
            admin_no = input("Enter admin number to view: ").strip()
            grades = gradebook.view_student_grades(admin_no)
            if grades:
                student = gradebook.get_student(admin_no)
                print(f"\nGrades for {student.name} ({admin_no}):")
                for subject, mark in grades.items():
                    print(f"{subject}: {mark}")
            else:
                print("Student not found.")

        elif choice == '5':
            admin_no = input("Enter admin number to edit: ").strip()
            student = gradebook.get_student(admin_no)
            if student:
                subject = input("Enter subject to edit (Math/Science/SST/English): ").strip()
                if subject in student.marks:
                    try:
                        new_marks = int(input("Enter new marks (0-100): "))
                        if student.edit_marks(subject, new_marks):
                            gradebook.save_data()
                            print(f"Marks updated successfully.")
                        else:
                            print("Invalid marks. Must be between 0 and 100.")
                    except ValueError:
                        print("Please enter a valid number.")
                else:
                    print("Invalid subject.")
            else:
                print("Student not found.")

        elif choice == '6':
            details = gradebook.print_gradebook()
            print(f"\nTotal Students: {details['total_students']}")
            print("\nStudent Details:")
            for admin_no, name in details['student_details'].items():
                grades = gradebook.view_student_grades(admin_no)
                print(f"Admin No: {admin_no}, Name: {name}")
                for subject, mark in grades.items():
                    print(f"  {subject}: {mark}")

        elif choice == 'm':
            continue
        
        elif choice == 'c':
            os.system('cls' if os.name == 'nt' else 'clear')
            
        elif choice == 'q':
            print("Saving data and exiting the system. Goodbye!")
            gradebook.save_data()
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()