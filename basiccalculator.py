name = input("Enter your name: ")
student_number = int(input("Enter your student number: "))
def calculate_cgpa():
    # Get student details
    marks = []
    credit_units = []
    for i in range(4):
        marks.append(int(input(f"Enter marks for course {i+1}: ")))
        credit_units.append(int(input(f"Enter credit units for course {i+1}: ")))

    # Grade conversion and grade points
    grades = []
    grade_points = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
    for mark in marks:
        if mark >= 90:
            grades.append('A')
        elif mark >= 80:
            grades.append('B')
        elif mark >= 70:
            grades.append('C')
        elif mark >= 60:
            grades.append('D')
        elif mark >= 50:
            grades.append('E')
        else:
            grades.append('F')

    # Calculate CGPA
    total_grade_points = sum([grade_points[grade] * credit for grade, credit in zip(grades, credit_units)])
    total_credit_units = sum(credit_units)
    cgpa = total_grade_points / total_credit_units

    print(f"CGPA for {name} is: {cgpa:.2f}")

def basic_calculator(student_number):
    # Extract last two digits from student number
    num1 = student_number % 10
    num2 = (student_number // 10) % 10

    # Perform arithmetic operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else "Error: Division by zero"

    print(f"Basic Calculator Results:")
    print(f"Addition: {num1} + {num2} = {addition}")
    print(f"Subtraction: {num1} - {num2} = {subtraction}")
    print(f"Multiplication: {num1} * {num2} = {multiplication}")
    print(f"Division: {num1} / {num2} = {division}")

# Run the program
calculate_cgpa()
basic_calculator(int(student_number))

   

   

 
