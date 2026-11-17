# 1. Take two numbers from the user and perform addition, subtraction, multiplication and division.
a = 2
b = 4

add = a + b 
sub =  a- b
mul = a * b
div = a / b 
print("add :" , add , "sub :" , sub, "mul : " , mul , "div : " , div) 

# 2. Take two numbers and find their floor division.

a = 30
b = 4

print("Floor div = " , a // b )

# 3. Take two numbers and find their remainder.
print("Remainder : ",a % b )

# 4. Take a number and calculate its square and cube using the power operator
b = 5
print("square : " , b ** 2 , " \n" ,"cube :" , 5 ** 3)

# 5. Take a number and check whether it is greater than 50.
a = 34
print(a >= 50)

# 6. print whether the first number is greater than, less than or equal to the second.
a = 45
b =55

if a > b :
    print("A is greter : ")
elif b > a :
    print("B is greter : ") 
else:
    print("Both are same ")
           
# 7. Take a person's age and check whether it is between 18 and 60 (inclusive).

age = 34
if  age >= 18 or age <= 60:
    print("age is between 18 and 60")
    
# 8. Take two numbers and check whether both are positive using `and`.
a = 100 
b = 93
if a > 0 and b > 0 :
    print("Both Positive num ")
else :
    print("one or both are Negative num ")

# 9. Take a number and check whether it is divisible by either 3 or 5 using `or`.
a = 67 

if a % 3 == 0 or a % 5 == 0:
    print("divisible by either 3 or 5")
else:
    print("Not divisible by 5 ")

# 10. Take a number and use `not` to check whether it is not equal to zero.
a = 0

if not a == 0 : 
    print("not Equarl to zero")
else:
    print("equal to zero ")
    
# 11. check whether it is even using the modulus operator.
a = 67

if a % 10 == 0:
    print("Even ")
else :
    print("Odd ")
    
# 12. Take a number and check whether it is odd using the modulus operator.
a = 60

if a % 10 != 0:
    print("Odd ")
else :
    print("Even ")
    
# 13. Create a variable with value 100 and increase it by 25 using `+=`.
b = 100

c = b + 25
print(c)

# 14. Create a variable with value 100 and decrease it by 30 using `-=`.
b = 100

c = b + 30
print(c)

# 15. Create a variable with value 5 and multiply it by 4 using `*=`.
a = 5

c = a * 4
print(c)

# 16. Create a variable with value 20 and divide it by 4 using `/=`.
a = 20

c = a / 4
print(c)

# 17. Take a number and check whether it is divisible by both 2 and 5.
a = 37

if a % 2 == 0 and a % 5 == 0:
    print("Yes divisible")
    
# 18. Take a number and check whether it is divisible by 3 but not divisible by 5.
a = 40

if a % 3 == 0 and a % 5 != 0:
    print("divisible by 3 but not divisible by 5")
    
# 19. Create two variables with the same value and compare them using `==` and `is`.
a = 45
a = b
b = 45

print(a == b)
print(a is b)

# 20. Create a list of five numbers and check whether a given number exists in that list.
li = [56,78,34,98,68]

print(89 in li)

# 21. Create two variables referencing the same list and check their identity using `is`.
l1 = [45,78,564,34,2,34]
l2 = [56,765,54,343,]

print(l1 is l2)
# 22. Take a number and demonstrate the bitwise AND (`&`) operator.
a = 67
b = 8
print(b & a)
# 23. Take two numbers and demonstrate the bitwise OR (`|`) operator.
a = 67
b = 8
print(b | a)
# 24. Take a number and demonstrate left shift (`<<`) and right shift (`>>`).
a = 4
b = 3

print(a << b)
print(a >> b)
print(a & b)

# # 25. Take three numbers and perform an expression using arithmetic, comparison and logical operators together. Print the final Boolean result.

a = 6
b = 4
c = 4

print(((a * b ) / c) or (a >= b) or c != b  )
# # ## Section 2 – Conditional Statements (25 questions)
# # 1. Take a number and check whether it is positive.
a = 2
if a > 0 :
    print("Positive")
else:
    print("Negative")
    
# 2. Take a number and check whether it is negative or zero.
a = 2
if a < 0 :
    print("Negative")
else:
    print("Posive")
# 3. Take a number and check whether it is even or odd.

a = 5654

if a % 2 == 0 :
   print("Even")
else:
    print("Odd")
     
# 4. Take a person's age and check whether they are eligible to vote.
age = 78

if age >= 18 :
    print("You are eligible for vote")
else:
    print("not")
    
# 5. Take two numbers and print the greater number.
a = 45
b = 78

if a >b :
    print("A is greter")
else:
    print("B is greter")
# 6. Take two numbers and check whether both are equal.
a = 76
b = 98

if a == b:
    print("a is equals to b ")
else:
    print("Not equal")
    
# 7. Take three numbers and find the largest number.
a = 22
b = 89 
c = 465

if a > b and a > c:
    print("A is greter ")
elif b > a and b > c:
    print('B is greter')
else:
    print("C is greter")
    
# 8. Take a student's marks and check whether they passed (passing marks: 35).
marks = 48

if marks >= 35:
    print("passed")
else:
    print("failed")
    
# 9. Take marks and display a grade using 
# if-elif-else (90+: A, 75–89: B, 60–74: C, 35–59: D, below 35: Fail).

marks = 84

if marks >= 90:
    print("A grade")
elif marks <= 89 and marks >= 75:
    print("B grade")
elif marks >= 60 and marks <= 74:
    print("C grade")
elif marks >=35 and marks <= 59:
    print("D grade")
else:
    print("Failed")   
                
# 10. Take a number and check whether it is divisible by 5.

num = 34
if num % 5 == 0 :
    print("divisible")
else :
    print("Not divisible")
    
# 11. Take a number and check whether it is divisible by both 3 and 5.
num = 34
if num % 5 == 0 and num % 3 == 0:
    print("divisible")
else :
    print("Not divisible")
    
# 12. Take a year and check whether it is a leap year.
yrs = 2026
if yrs % 400 == 0:
    print("leap yrs")
elif yrs % 100:
    print("Not leap year")
elif yrs % 4:
    print("leap year")
else:
    print("Not leap year")

# 13. Take a character and check whether it is a vowel or consonant.
char = "a" 
vowel = ("a" , "e","i","o","u")

if char in vowel:
    
    print("Vowel : ", char)
else:
    print("Consonant: ",char)
    
# 14. Take a character and check whether it is uppercase or lowercase.
char = "p"
if char.islower():
    print("Lowercase")
else:
    print("Uppercase")
    
# 15. Take a number and check whether it is a two-digit number.
num = 24
if num >= 10 and num <= 99:
    print("Two digit num ")
else:
    print("Not two digit num")

# 16. Take a number and check whether it is between 100 and 999.
num = 342

if num > 100 and num > 999:
    print(num , "Is between 100 and 999")
# 17. Take three sides and check whether they can form a valid triangle.
s1 = 45
s2 = 43
s3 = 32
if s1 + s2 > s3 and s3 + s1 > s2 and  s2 + s3 > s1 :
    print("can built valid triangle")
else:
    print("can not buit ") 
       
# 18. Take a username and password and check whether both match predefined values.

u = "vaish" 
p = 123

username = "vaish" 
password = "12"

if username ==u and password == p:
    print("correct username and password ")
else:
    print("Enter valid password")
# 19. Create a simple ATM program: check balance and allow withdrawal only if sufficient balance is available.
balance = 50000

if balance >= 100:
    print("You can withdraw")
else :
    print("You can not insufficient balance is available")

# 20. Take a shopping bill amount and apply a discount using conditions.
amt = 15
disc = 2
total = 0

if amt > 5:
    total = (amt * disc) / 100
    final_amount = amt - total

    print("Original price:", amt)
    print("Discount amount:", total)
    print("Final amount:", final_amount)

else:
    print("No discount")
    
    
# 21. Take a number and check whether it is positive, negative or zero using a nested if.
num = 45

if num > 0:
    print("positive")
elif num < 0 :
    print("negative")
else:
    print("Zero")
    
# 22. Find the greater of two numbers using a ternary operator.
a = 45
b = 54
c = 23

greter = a if a > b and a > c else b if b > a and b > c else c
print("greter num is : " , greter)


# 23. Use a ternary operator to check whether a number is even or odd.
a = 45
num = "Even" if a % 2 == 0 else "odd"
print(num)

# 24. Create a simple calculator using `match-case` for addition, subtraction, multiplication and division.
A = 67
B = 63
operator = "+"

match operator :
    case  "+":
        print("Addition" , A + B)
    case "-":
        print("sub", A - B)
    case "/":
        print("Division", A / B)
    case "*":
        print("Multiplicaton", A * B)
                           
    
# 25. Create a menu-based program using `match-case` to display the selected day of the week.

day = 3

match  day:
    case 1:
        print("sun")
        
    case 2:
        print("mon")
    case 3 :
        print("tue")
    case 4 :
        print("wed")
    case 5 :
        print("fri")
    case 6 :
        print("sat")                   

# ## Section 3 – Loops (25 questions)


# 1. Print numbers from 1 to 10 using a for loop.

for i in range(1 , 11):
    print(i)

# 2. Print numbers from 10 to 1 using a for loop.

for i in range(11,0,-1):
    print(i)

# 3. Print even numbers from 1 to 50.

for i in range(1 , 51):
    if i % 2 == 0:
        print("Even")
    else:
        print("odd", i)
# 4. Print odd numbers from 1 to 50.

for i in range(1 , 51):
    if i % 2 != 0:
        print("Odd", i)
        
# 5. Print multiples of 5 from 1 to 100.
for i in range(1,101):
    if i % 5 ==0:
        print(i)
# 6. Calculate the sum of numbers from 1 to 10.
sum = 0

for i in range(1,11):
    sum = sum + i
print("Sum of num is :" , sum)

# 7. Calculate the sum of even numbers from 1 to 50.
sum = 0
for i in range(1 , 51):
    if i % 2 == 0:
        sum = sum + i
print("sum of even numbers is : " ,sum )

# 8. Calculate the sum of odd numbers from 1 to 50.
sum = 0

for i in range(1 , 51):
    if i % 2 != 0:
        sum = sum + i
print("sum of odd numbers is : " ,sum )

# 9. Print the multiplication table of a number entered by the user.
num = 8 

for i in range(1,11):
    digit = num * i
    print(num , " X " , i , " = " , digit)
        
# 10. Print the squares of numbers from 1 to 10.

for i in range(1 ,11):
    sq = i * i
    print(i ," = " , sq)

# 11. Count how many numbers between 1 and 100 are divisible by both 3 and 5.
count = 1
for i in range(1,101):
    if i % 3 and i % 5:
        count += 1
print(count)

# 12. Calculate the factorial of a number.
fact = 1
num = 5

for i in range(1 , num +1):
    fact = fact * i
    print(fact)

# 13. Count the digits in a number.

num = 1234
count = 0

for i in str(num):
    digit = num % 10 
    count = count + 1
    num = num // 10
print(count)    
    
# 14. Find the sum of digits of a number.
num = 1234
sum = 0
i = 1

# for i in str(num):
# sum = sum + int(i)
# print(sum) 

# 15. Reverse a given number.

num = 1234
count = 0
reverse = 0

for i in str(num):
    digit = num % 10 
    reverse = reverse * 10 + digit
    num = num // 10
print(reverse) 

# 16. Check whether a number is a palindrome.

num = 1234

original = 0

for i in str(num):
    digit = num % 10 
    reverse = reverse * 10 + digit
    num = num // 10
if original == num:
    print("Palindrome")


# 17. Print the Fibonacci series for a given number of terms.
fib = 5

a = 0
b = 1

for i in range(fib):
    print(a)
    c = a + b
    a = b
    b = c 
# # 18. Check whether a number is prime.
num = 7

if num <= 1:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

# Print all prime numbers between 1 and 100

for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)


# 20. Print numbers from 1 to 20 using a while loop.
num = 9
i = 0
while i<=20:
    print(i)
    i+1
    
# 21. Calculate the sum of numbers from 1 to N using a while loop.
n = 10
sum= 0
for i in range(n):
    sum = sum+i
print(sum)
# 22. Print numbers from 1 to 20 but skip multiples of 3 using `continue`.
for i in range(1,20):
    if i % 3 == 0:
        continue
    print(i)
# 23. Print numbers from 1 onwards and stop when the number reaches 10 using `break`.
for i in range(0,0):
    if i == 10:
        break
    print(i)

# 24. Print this pattern:
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
# # 25. Print this multiplication pattern using nested loops:

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# ## Section 4 – Other Core Python Basics (25 questions)


# 1. Create variables of int, float, string, Boolean and complex types. Print their values and types.
i = 12
j= 12.4
k="vaish"
y=True
z = 4 + 2j
print(i,type(i))
print(j,type(j))
print(k,type(k))
print(y,type(y))
# # 2. Take a name and age from the user and print them in a formatted sentence.
name = "vaish"
age = 21

print(f"my name is : {name}")
# # 3. Take two numbers as input, convert them into integers and print their sum.
v = 23
g = 25

print(v + g)
# # 4. Demonstrate `sep` and `end` in a single program.
name = "vaishnavi is improving"

print(sep=" - " , end=" | ")

# # 5. Create two variables and display their memory identity using `id()`.
l1 = [1,141,56]
l2 = [1,141,56]

print(id(l1))
print(id(l2))
# # 6. Demonstrate the difference between `==` and `is` using two separate list objects.
l1 = [1,141,56]
l2 = [1,141,56]

print(l1==l2)
print(l1 is l2)

# # **B. Strings and slicing**

# # 7. Take a string and print its first and last characters using indexing.
name = "vaishnavi"
print(name[0:1])
print(name[-1])

# # 8. Print a string in reverse using slicing.
name = "vaish"
print(name[::-1])

# # 9. Print the first three characters of a string.
name = "vaish"
print(name[:3])
# # 10. Print the last three characters of a string.
name = "vasih"
print(name[-3])
# # 11. Print every second character using slicing.
name = "vasihnai is breaking her limits"
print(name[::2])
# # 12. Convert a string into uppercase and lowercase.
name = "vasih"
print(name.lower())
print(name.upper())
# # 13. Count the number of characters in a string using `len()`.
str = "vaish"
print(len(str))
# # 14. Take a sentence and replace all spaces with hyphens.
setence = "i am vaish"
s = setence.replace(" ", "-")
print(s)
# # 15. Take a sentence and split it into individual words.
# st = "hello ", "world"
# print(split(str))
# print(s)
# # 16. Remove extra spaces from the beginning and end of a string using `strip()`.strr
strr = "  VASIH         "
print(strr.strip())

# **C. Lists and tuples**

# 17. Create a list of five numbers and print each element using indexing.
li = [ 12,45,56,33,23]
for i in range(len(li)):
    print(li[i])
# 18. Add two new elements to a list using `append()` and `extend()`.
li = [ 12,45,56,33,23]
li.append(34)
print(li)

li.extend([56,65,78])
print(li)

# 19. Remove an element using `remove()` and another using `pop()`.

# li.remove(45)
li.pop(2)
print(li)



# # 20. Find the largest, smallest and sum of all elements in a list.
# li = [ 12,45,56,33,23]
# print(sum(li))
# print(max(li))

# print(min(li))

# 21. Create a list and print its elements in reverse order using slicing.
li = [ 12,45,56,33,23]

print(li[::-1])
    
# 22. Create a tuple of five elements and access 
# its second and last elements.

tup = (12,43,22,1,1)

print(tup[2])
print(tup[-1])

# 23. Create a tuple and unpack its values into separate variables.
tup = (12,43,22,1,1)

first, * middle , last = tup

print(first)
print(last)
print(middle)

# 24. Create a set containing duplicate numbers and 
# demonstrate how duplicates are handled. Then perform union and # intersection on two sets

# Demonstrate duplicate removal
s1 = {12, 56, 12, 98, 12}

print(s1)

# Create another set
s2 = {56, 78, 98, 100}

# Union
print("Union:", s1.union(s2))

# Intersection
print("Intersection:", s1.intersection(s2))

# 25. Create a dictionary of five students and their marks. 
# Add a new student, update one student's marks, print all keys and values, 
# and find the student with the highest marks.

dic = {"vaish": 98 , "nick" : 78, "alice" : 87}

print(dic.update({"danny: 84"}))
# Find the student with the highest marks
highest = max(dic, key=dic.get)

print("Highest scorer:", highest)
print("Marks:", dic[highest])
