num = -5 

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

year = 2024 

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

num1 = 10
num2 = 5
operator = '+'  
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2 if num2 != 0 else "Error! Division by zero."
else:
    result = "Invalid operator."

print(f"Result: {result}")

marks = 78  

if marks >= 85:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"

print(f"Student's grade: {grade}")