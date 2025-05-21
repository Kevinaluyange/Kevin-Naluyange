def get_student_details():

    name = input("Enter your name: ")
    student_number = input("Enter your student number: ")
    marks = []

    # Collect marks for four courses
    for i in range(1, 5):
        mark = int(input(f"Enter marks for course {i}: "))
        marks.append(mark)

    return name, student_number, marks

def convert_student_number(student_number):
    # Converts student number into two numbers
    num1 = int(student_number[:len(student_number)//2])
    num2 = int(student_number[len(student_number)//2:])
    return num1, num2

def basic_calculator(num1, num2):
    # Performs arithmetic operations
    operation = input("Choose an operation (+, -, *, /): ")
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2 if num2 != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

def convert_marks_to_grades(marks):
    
    grades = []
    for mark in marks:
        if 90 <= mark <= 100:
            grades.append('A')
        elif 80 <= mark <= 89:
            grades.append('B')
        elif 70 <= mark <= 79:
            grades.append('C')
        elif 60 <= mark <= 69:
            grades.append('D')
        elif 50 <= mark <= 59:
            grades.append('E')
        else:
            grades.append('F')
    return grades

def calculate_grade_points(grades):
    # Assigns grade points
    grade_points = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
    points = [grade_points[grade] for grade in grades]
    return points

def calculate_cgpa(points):
    
    cgpa = sum(points) / len(points)
    return cgpa

# Main function
def main():
    name, student_number, marks = get_student_details()

    num1, num2 = convert_student_number(student_number)
    print(f"\nNumbers derived from student number: {num1}, {num2}")
    
    result = basic_calculator(num1, num2)
    print(f"\nResult of the operation: {result}")

    grades = convert_marks_to_grades(marks)
    print(f"\nGrades: {grades}")

    points = calculate_grade_points(grades)
    cgpa = calculate_cgpa(points)
    
    # Print final student details and results
    print(f"\nStudent Name: {name}")
    print(f"Student Number: {student_number}")
    print(f"Grades: {grades}")
    print(f"CGPA: {cgpa:.2f}")

# Runs the main function
if __name__ == "__main__":
    main()
