
# `student_id, student_name, email, phone, date_of_birth, gender, course, city, admission_date, percentage`

student_id = int(input("Enter Student id :"))
student_name = input("Enter your name : ")
Email = input("Enter Your Email  : ")
Phone = (input("Enter Your Phone No : "))
Date_of_birth = (input("Enter your Date_of_Birth : "))
Gender = input("Enter your gender : ")
Course = input("Enter Your  Course:")
City = input("Enter Your city :")
Admission_date = input("Enter your admission date : ")
percentage = float(input("Enter your percentage : "))


print("Your id is : ",student_id)
print("Your name is : " , student_name)
print(Email)
print(Phone)
print(Date_of_birth , sep = '-')
print(Course)
print(Gender,Course,City,Admission_date, sep = '\n')
print(percentage , end = "%")


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

# Arithematic operator 


# # exercise : 

# #Q1-Calculate the total price of 5 notebooks if one notebook costs â‚¹40.

quantity = int(input("Enter quantity : "))
notebook = int(input("Enter price of Noteboooks "))

print("Total price of  5 notebook is : " ,quantity , " * " , notebook , " = "  , quantity * notebook )


#Q2-Calculate the remaining balance after spending â‚¹350 from â‚¹1,000.

balance_A = 350
balance_B = 1000 

print("Remaining Balance after spending : " ,balance_B , " - " , balance_A , " = "  , balance_B- balance_A )

# #Q3-Calculate the area of a rectangle with length 15 and width 8.

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


print(not(True)and 31>= 34 or not (32>21 and (True))and not(True or 56 != 0))

print(not(0==0)and 34 >= 34 or not(32 > 21 and not (False) or 0 != 0))

print(("Ram" == "ram") and (0>0) and 34 != 34 or not (32 > 21 and not(True)) and not(True or 56 != 0))

print(not(False)and 34 != 34 or not (int("32") >= 21 and not (True)) and not (True or 0.1 != 0))

print(not(False) and 34 <=0 or not(32 >= 21 and not ("""sahil""" == """sahil""")) and not (True or 56 != 0))




# Python Practice: Arithmetic & Comparison Operators

# Q1. Shopping

# A notebook costs ₹40. You buy 5 notebooks.

# Calculate the total price.

# notebook = int(input("Enter cost of notebook : "))
# quantity = int(input("Enter quantity : "))

# print("Your total price is : " , notebook * quantity)


# Q2. Salary

# Your monthly salary is ₹25,000.

# Calculate your annual salary.

salary = int(input("Enter your monthly salary : "))

print("Your annual salary is : ", salary * 12)


# Q3. Restaurant Bill

# A restaurant bill is ₹850

# You and 4 friends split the bill equally.

# Calculate how much each person pays.

bill = 850 
friends = 4

print("Bill after split is : " , bill / friends)

# # Q4. Travel

# # You travel 120 km in 3 hours.

# # Calculate your average speed.

# # Formula: speed = distance / time

distance = 120 
time = 3

print("Your avrg speed is : " , distance/time )

# Q5. Age Verification

# A person is 19 years old.

# Check whether the person is 18 or older.

# Expected output: True / False

age = 19 

print ( age >= 18)

# Q6. Shopping Budget

# You have ₹2,000.

# Shoes cost ₹1,799.

# Check whether you can afford the shoes.

total_money = 2000
shoes_cost = 1799

print(total_money >= shoes_cost)



# Q7. Exam

# A student scored 72 marks.

# Check whether the marks are greater than 60.

marks = 72
print(marks >=60 )

if marks> 60 :
      print("Your Marks are greter than 60 ")

# Q8. Temperature

# Today's temperature is 38°C.

# Check whether the temperature is greater than 40°C.

temp = 38

print(temp > 40)


# Q9. Discount

# A shirt costs ₹1,500.
# Your budget is ₹1,200.
# The shop gives a ₹400 discount.
# Calculate the final price.
# Check whether you can buy the shirt within your budget.
# Expected:
# # Final Price: ___

# # Can Buy: True / False

shirt_cost = 1500
budget = 1200
discount = 400

print(shirt_cost - discount <= budget)   


# Q10. Exam Result

# A student gets:

# English = 75

# Python = 82

# SQL = 68

# Calculate the total marks.

# Check whether the total is greater than or equal to 200.


Python = 82
Eng = 75
SQL = 68

print((Python + Eng + SQL) > 200)

# Q11. Monthly Expense

# Calculate the remaining money.

# Check whether the person saved more than ₹10,000.
Monthly_income = 30000
Rent = 9000
Food = 5000
Travel = 2000
Other = 3000

expenses = Rent + Food + Travel + Other
remaining_money = Monthly_income - expenses

print("Remaining money:", remaining_money)
print("Saved more than 10000:", remaining_money > 10000)


# Q12. Employee Salary

# Employee A = ₹35,000

# Employee B = ₹42,000

# Check:

# 1. Is A's salary greater than B's?

# 2. Is A's salary less than B's?

# 3. Are their salaries equal?

# 4. Is B's salary greater than or equal to ₹40,000?

Employee_A = 35000

Employee_B = 42000

if Employee_A > Employee_B :
      print("A'salary is greter than B's Salary ")
      
else :
      print("Not greter than ") #just tried solve using conditions too dont give error bro please
print(Employee_A > Employee_B)
print(Employee_A < Employee_B)
print(Employee_A == Employee_B)
print(Employee_B >= 40000)


# Q13. Product Comparison

# Laptop A = ₹55,000

# Laptop B = ₹65,000

# Check:

# 1. Laptop A < Laptop B

# 2. Laptop B > Laptop A

# 3. Laptop A == Laptop B

# 4. Laptop A != Laptop B
laptop_a = 55000
laptop_b = 65000

print(laptop_a < laptop_b)
print(laptop_b > laptop_a)
print(laptop_a == laptop_b)
print(laptop_a != laptop_b)


# Q14. AND Operator

# A person can enter an event only if:

# - Age is 18 or more

# - AND ticket price is less than or equal to ₹500

age = 21
ticket = 150 

print(age >= 18 and ticket <= 500)

# Given:

# age = 21

# ticket_price = 450

# Create ONE condition to check both requirements.

# Q15. OR Operator

# A student gets a scholarship if:

# - Marks are 90 or more

# - OR attendance is 95 or more
marks = 87

attendance = 97

print(marks >= 90 or attendance>= 95)


# Q16. Mixed Real-Life Problem

# A company wants to hire a candidate if:

# - Age is between 21 and 30

# - AND Python score is at least 70

# - AND SQL score is at least 60

# Given:

# age = 24

# python_score = 75

# sql_score = 62

# Write ONE Python condition to determine eligibility.
age = 24 
python_score = 75
sql_score = 62 

print(age >= 21 and age <= 30 and python_score >= 70 and sql_score >= 60)

# Take two numbers from the user and check whether they are equal
a = int(input("Enter A : "))
b = int(input("Enter B : "))

print("A is equals to B : ",a == b)
print("A is not equals to B : ", a != b)

# Take two numbers and check which comparison results are True.
a = int(input("Enter A : "))
b = int(input("Enter B : "))

print("A is equals to B : " , a ==b )
print("A is not equals to B : " , a != b )
print("A is greter than B : " , a > b )
print("A is less to B : " , a < b )
print("A is greter equals to B : " , a >=b )
print("A is less equals to B : " , a <= b )

# Take a person's age and check whether the age is greater than 18
age = int(input("Enter Your age : ") )

print("Your ages is greter than 18 ", age > 18)
print("Your ages is greter not than 18 ", age < 18)

# Take two numbers and check whether they are different.

a = int(input("Enter A : "))
b = int(input("Enter B : "))

print("num same : ", a == b)
print("num different : ", a != b)

# Take a student's marks and check whether marks are greater than or equal to 40.

a = int(input("Enter marks a : "))
b = int(input("Enter marks b : "))

print("marks are greter : " , a > 40 )
print("marks are equals : " , a == 40)

# Take two numbers and display the result of all six comparison operators.
a = int(input("Enter marks a : "))
b = int(input("Enter marks b : "))

print("a is greter than b " , a > b)
print("a is less than b " , a < b)
print("a is greter than or equals to b " , a >= b)
print("a is less than or equals to b " , a <= b)
print("a is equals to b " , a == b)
print("a is not equals to b " , a != b)

# Practise Questions on logical Operator : 

a = 10 
b = 20 
print(a > b and b > 15) #false

#Q
a = 10
b = 20
print(a > b or b > 15) #True

#Q
a = 10
b = 20
print(not(a > b)) #True

# Q4
age = 25
print(age >= 18 and age <= 60) #True

# Q5 

marks = 35

print(marks >= 40 or marks == 35) #True
# Q6 Take age and salary from the user and check:
# age >= 18 AND salary >= 20000

age = int(input("Enter age : "))
salary = int(input("Enter salary : "))

print(age >= 18 and salary >= 20000) 
# AND salary >= 20000)


# Q7 Take two numbers from the user and check whether:
#    first number is greater than 10 OR
#    second number is greater than 10 

a = int(input("Enter number a : "))
b = int(input("Enter number b : "))

print(a>10 or b >10 )


