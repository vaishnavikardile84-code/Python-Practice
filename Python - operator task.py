
# exercise : 

#Q1-Calculate the total price of 5 notebooks if one notebook costs â‚¹40.

quantity = int(input("Enter quantity : "))
notebook = int(input("Enter price of Noteboooks "))

print("Total price of  5 notebook is : " ,quantity , " * " , notebook , " = "  , quantity * notebook )


#Q2-Calculate the remaining balance after spending â‚¹350 from â‚¹1,000.

balance_A = 350
balance_B = 1000 

print("Remaining Balance after spending : " ,balance_B , " - " , balance_A , " = "  , balance_B- balance_A )

#Q3-Calculate the area of a rectangle with length 15 and width 8.

Length = 15
Width = 8

print("Are of reactangle is : " , Length , " * " , Width , " = ", Length * Width)

#Q4-Divide 57 chocolates equally among 6 students and display the quotient and remainder.

Chocolates = 57 
Students = 6

print("Divided 57 Chocolates into 6 studetns : " , Chocolates , " / " , Students , " ="  , Chocolates / Students )
print("remainder is : " , Chocolates , " % " , Students ," = "  , Chocolates % Students )



#Q5-Convert a total number of minutes, such as 135, into hours and remaining minutes using // and %.
TMinutes = 135 
HMin = 60

print("Total number of HOURS : " , TMinutes // HMin, "Remainder is : " , TMinutes % HMin)

#Q6-Calculate the average of three numbers using arithmetic operators.

a = 25
b = 50 
c = 10

print("Average of a , b , c is : " , (a * b * c)/3 )


a = 2
b = 3
c = 2

print("Exponentiation by using ternary operator : " , a ** b ** c)

#------------------------------------------------------SATURDAY TASK-----------------------------------------------------------------------------------------

# <!-- for batch 1342 python : 


# Python Practice on Variables + input() + print()
# 1. Student Information
# Take the following information from the user and print it:
# - Name
# - Age
# - College name
# - Course

Name = input("Enter Your Name : ")
Age = int(input("Enter Your Age : "))
Collage = input("Enter Your Collage Name : ")
Course = input("Enter Your Course Name : ")

print("Your Name is : " , Name)
print("Your Age is ", Age)
print("Your Course is : ", Course)
print("Your collage is : " , Collage)


# 2. Employee Details
# Take input for:
# - Employee name
# - Employee ID
# - Department
# - Salary
# Print all employee details in a proper format.

Emp_Name = input("Enter Emp_Name : ")
Emp_id = int(input("Enter Your id : "))
Department = input("Enter Your Department Name : ")
Salary = int(input("Enter Your Salary : "))

print("Your Emp_Name is : " , Emp_Name, "Emp_id is :" , Emp_id , "Department is : " , Department , " Salary is :" , Salary , sep="\n")


# 3. Personal Introduction
# Take input for:
# - First name
# - Last name
# - City
# - Profession
# Print a complete introduction using the entered values.
First_name = input("Enter Your First Name : ")
Last_name = input("Enter Your Last Name : ")
City = input("Enter Your City : ")
Profession = input("Enter Your Profession : ")

print("Your First name is : " , First_name , " Your Last Name is : " , Last_name , " Your City is : " , City ," Your Profession is : " , Profession , sep="\n")



# 4. Two Numbers
# Take two numbers from the user and store them in two variables. Print both values.
# Example:
First_num = int(input("Enter first number"))
Second_num = int(input("Enter second number"))

print("First num = ",First_num , sep = "\n")
print("Second_num = ",Second_num)


# 5. Basic Addition
# Take two numbers from the user and calculate their addition.
# Example:
# Enter first number: 20
# Enter second number: 30
# Addition = 50

First_num = int(input("Enter first number: "))
Second_num = int(input("Enter second number: "))

print("First num =", First_num,
      "Second num =", Second_num,
      "Addition of Both num =", First_num + Second_num,
      sep="\n")

# 6. Student Marks
# Take marks of three subjects from the user and calculate:
# - Total marks
# - Average marks
# Print the result.

English_Marks = int(input("Enter Your Eng Marks : "))
Mathematics_Marks = int(input("Enter Your Math Marks : "))
Hindi_Marks = int(input("Enter YOur Hindi Marks : "))

print("Your total marks are : " , English_Marks + Mathematics_Marks + Hindi_Marks , "Your Average Score is : ", (English_Marks + Mathematics_Marks + Hindi_Marks ) / 3 , sep = "\n" )


# 7. Rectangle Calculation
# Take length and width from the user and calculate:
# - Area
# - Perimeter

Length = 15
Width = 8

Length = int(input("Enter length "))
Width = int(input("Enter Width"))

print("Are of reactangle is : " , Length , " * " , Width , " = ", Length * Width , "Perimeter of Rect is : " , (Length + Width) * 2  , sep = "\n");





# 8. Salary Calculation
# Take the following from the user:
# - Basic salary
# - HRA
# - DA
# Calculate and print the total salary.


Basic_salary = int(input("Enter Your Basic Salary : " ))
HRA = int(input("Enter Your HRA Salary : " ))
DA = int(input("Enter Your DA Salary : " ))

print("Basic Salary is : "  , Basic_salary)
print("Basic HRA is : "  , HRA)
print("Basic DA is : "  , DA)


print("Total salary is " ,Basic_salary + HRA + DA )


# 9. Shopping Bill
# Take input for:
# - Product name
# - Price
# - Quantity
# Calculate and print the total amount.
# Example:
# Product: Pen
# Price: 20
# Quantity: 5
# Total Amount = 100

Products = input("Enter Your Product Name : ")
Price = int(input("Enter Your price  : "))
quantity = int(input("Enter Quantity : "))

print("Product name : " , Products , "Price is : " , Price , "quantity is : " , quantity ,  "Total amount : " ,Price * quantity , sep = "\n")

# 10. Temperature Conversion 
# Take temperature in Celsius from the user and convert it into Fahrenheit. -->

Celsius = float(input("Enter celsius valuse : "))

print("Temperature in Fahrenheitis is : ", (Celsius * 9 /5 ) + 32  )




