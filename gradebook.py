import os
your_reg_number = '18/U/23394/EVE' #update your registration number
your_name = 'NALUYANGE KEVIN' #update your name

class Gradebook:
    def __init__(self):
        self.students = {}

    def add_student(self, admin_no, name, math, science, sst, english):
        #fuction to add students
        if admin_no in self.students:
            print("Admin number already exists.")
            return
        self.students[admin_no] = {
            'Name': name,
            'Math': math,
            'Science': science,
            'SST': sst,
            'English': english
        }
        print(f"Student {name} added successfully.")
        print(self.students)

    def delete_student(self, admin_no):
        #function to delete students from grade book
        if admin_no in self.students:
            del self.students[admin_no]
            print(f"Student with admin number {admin_no} deleted successfully.")
        else:
            print("Admin number not found.")

    def view_statistics(self):
        #function to view statistics such as mean, mode, max and min mark
        if not self.students:
            print("No students in the gradebook.")
            return
        subjects = ['Math', 'SST', 'English']
        for subject in subjects:
            marks = [student[subject] for student in self.students.values()]
            if marks:
                print(f"{subject} - Mean: {sum(marks)/len(marks):.2f}, Mode: {max(set(marks), key = marks.count)}, Max: {max(marks)}, Min: {min(marks)}")
            else:
                print(f"No marks available for {subject}.")
    
    def view_student(self, admin_no):
        #function to view student details
        if admin_no in self.students:
            student = self.students[admin_no]
            print(f"Admin No: {admin_no}, Name: {student['Name']}, Math: {student['Math']}, Science: {student['Science']}, SST: {student['SST']}, English: {student['English']}")
        else:
            print("Admin number not found.")

    def edit_student(self, admin_no, subject, new_mark):
        #function to edit student info
        if admin_no in self.students:
            if subject in self.students[admin_no]:
                self.students[admin_no][subject] = new_mark
                print(f"{subject} mark updated to {new_mark} for student with admin number {admin_no}.")
            else:
                print("Invalid subject.")
        else:
            print("Admin number not found.")

    def print_gradebook(self):
        #function to print out the gradebook
        if not self.students:
            print("No students in the gradebook.")
            return
        for admin_no, student in self.students.items():
            print(f"Admin No: {admin_no}, Name: {student['Name']}, Math: {student['Math']}, Science: {student['Science']}, SST: {student['SST']}, English: {student['English']}")

    def clear_screen(self):
        #function to clear screen
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_menu(self):
        print("--------------------Menu--------------------")
        print("1 - Add student with marks")
        print("2 - Delete student, given an admin_no")
        print("3 - View statistics about the grades")
        print("4 - View student grades")
        print("5 - Edit student grades")
        print("6 - Print Gradebook")
        print("m - Print menu")
        print("c - Clear Screen")
        print("q - Quit system\n")

print()
print(f"Welcome to students Gradebook\nBy".upper())
print(f"{your_name} - {your_reg_number}\n")


#initialize the gradebook

gradebook = Gradebook()
gradebook.print_menu()

while True:
    choice = input("\n--------------------\nEnter your choice\n")
    
    if choice == '1':
       #Code to add a student. Teacher should supply admin_no, name and marks for SST, Maths, science and Eng
       admin_no = input("Enter admin number: ")
       name = input("Enter student name: ")
       math = int(input("Enter Math mark: "))
       science = int(input("Enter Science mark: "))
       sst = int(input("Enter SST mark: "))
       english = int(input("Enter English mark: "))
       gradebook.add_student(admin_no, name, math, science, sst, english)
        #Include details for added student and current number of students in grade book.
    
    elif choice == '2':
         #Add Code to delete a student. 
        admin_no = input("Enter admin number to delete: ")
        gradebook.delete_student(admin_no)
    
    elif choice == '3':
        #Add Code to give the gradebook statistics
         gradebook.view_statistics()
    
    elif choice == '4':
        #code to view student grades
        admin_no = input("Enter admin number to view: ")
        gradebook.view_student(admin_no)
    
    elif choice == '5':
        #code to edit students grades
        admin_no = input("Enter admin number to edit: ")
        subject = input("Enter subject to edit (Math, Science, SST, English): ")
        new_mark = int(input("Enter new mark: "))
        gradebook.edit_student(admin_no, subject, new_mark)

    elif choice == '6':
        #code to print the grade book
        gradebook.print_gradebook()   

    elif choice == 'm':
        gradebook.print_menu()
    
    elif choice == 'c':
        gradebook.clear_screen()
        os.system('cls') #Only for windows
        
    elif choice == 'q':
      print('Bye bye')
      break
    else:
        print('Invalid choice.')




