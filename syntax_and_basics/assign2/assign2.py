
try:
    a=float(input("Enter a: "))
    b=float(input("Enter b: "))
    print("Addition: a+b: ",int(a+b))
    print("Subtraction: a-b: ",int(a-b))
    print("Multiplication: a+b: ",a*b)
    print("Division: a+b: ",a/b)
except ValueError:
    print("Invalid input! Please enter a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")