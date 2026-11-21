# Q1. STUDENT INFORMATION
# Create a function named student_info().
# Accept name, age, and course as parameters.
# Pass all three values using positional arguments.
# Display student information.

def student_info(name, age, course):
    print("Student Name:", name)
    print("Student Age:", age)
    print("Student Course:", course)

student_info("Vaishnavi", 22, "BCA") 

# Q2. EMPLOYEE SALARY
# Create a function named employee_salary().
# Accept employee name, basic salary, and bonus.
# Calculate total salary.
# Call the function using keyword arguments.
# Change the order of keyword arguments when calling the function.

def employee_salary(name,salary,bonus):
    
    print("total salary: " , salary + bonus)
    
    print(name)
    print(salary)
    print(bonus)
    
employee_salary(salary = 25000 ,name = "Rahul", bonus = 5000)    
    
# Q3. SHOPPING BILL
# Create a function named shopping_bill().
# Accept product name, quantity, and price.
# Calculate the total bill.
# Call the function using both positional and keyword arguments.

def Shopping_bill(name, quantity,price):
    
    print("name : " , name)
    print("total prise" , quantity * price)
    
Shopping_bill("vaish",3,200)    

# Q4. CALCULATOR USING NESTED FUNCTIONS
# Create an outer function named calculator().
# Create four inner functions:
# addition()
# subtraction()
# multiplication()
# division()
# Perform all four operations using two numbers.
# Call all inner functions through the outer function.

def calculater(a,b):
    def add():
        print("addition" ,a + b)
    def sub():
        print("subtraction", a - b)
    def mul():
        print("multiplicaton" , a * b )
    def division():
        print("division", a / b )                    

    add()
    sub()
    mul()
    division()
calculater(2,5)