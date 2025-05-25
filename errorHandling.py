while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter second number: "))
        
        result = int(num1 / num2)
    except ValueError:
        print("Invalid input, please enter integral values.")
    
    except ZeroDivisionError:
        print("Cannot divide by zero, try entering another value.")

    else:
        print(f"The result of dividing {num1} by {num2} is {result}")
        break

    #finally:
     #   print("DONE!")