# syntax 
for i in range(10,0,-1):
    print(i)
    
num = 1234 
for i in range(num-1):
    print(i)
    

for i in range(1,6):
  
    print("Number" , i , "Square" , i ** 2 )    
sum = 0  
for i in range(1 , 6):
    sum = sum + i
print(sum)    

sum = 0 
for i in range(1 , 11):
    if i % 2 == 0 :
        # print(i)
        sum = sum +i
print(sum)        

count = 0        
for i in range(1 , 21):
    if i % 2 == 0 :
        count = count + 1
print(count)        

for i in range(10,0,-1):
    print(i)
    
for i in range(1,51,2):    
    if i % 2 != 0:
        print(i)
for i in range(1,101,5):        
    
    print(i)
    
n = 10
tbl = 0
for i in range(1 , 11):
    tbl = n * i
    print(n , "X", i , " = " , tbl)
    # print(tbl) 
    
for i in range(1,11):
    cube = i ** 3 
    print(cube)
    
    
for i in range(1,21):
    if i == 10 :
        continue
    print(i) 

sum = 0

for i in range(1 , 11):
    sum = sum + i
print(sum)
        
sum = 0
for i in range(1,101):
    if i % 2 != 0:
        sum = sum + i
print(sum)

product = 1 

for i in range(1 , 6):
    product = product * i
print(product)


count = 0
for i in range(1 , 101):
    if i % 3 == 0:
        # print(i)
        
        count = count + i
print(count)    
        
count = 0
        
for i in range(1 , 21):
    if i % 2 == 0 :
        count = count + 1
print(count)  

count = 0

for i in range(1, 101):
    if i % 3 == 0:
        # print(i)
        count = count + 1

print(count) 






# LEVEL 2: Variables and Calculations

# **Q16. Count Numbers Divisible by Both 3 and 5**

# Write a Python program using a `for` loop to count how many numbers from 1 to 100 are divisible by both 3 and 5

count = 0

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        count = count + 1

print(count)     

# **Q17. Sum of Squares**

# Calculate the sum of the squares of numbers from 1 to 10.

sum = 0
for i in range(1, 11):
    i = i ** 2
    print(i)
    sum = sum + i
print(sum)  
  
# **Q18. Average of Numbers**

# # Calculate the average of numbers from 1 to 10 using a `for` loop.

sum = 0
count = 0

for i in range(1 , 11):
    sum = sum + i
# print(sum)
    count = count + 1
avg = sum / count
print(avg)   

# **Q19. Sum of User Inputs**

# Take 5 numbers from the user using `input()` and calculate their sum.

total = 0
for i in range(1,6):
    i = int(input("Enter number : "))
    total = total + i
print(total)             
    
# **Q20. Count Positive, Negative, and Zero Values**

# for i in range(1 , 11):
# Take 10 numbers from the user. Count how many are positive, how many are negative, and how many are zero.

posit_counter = 0
neg_counter = 0
zero_counter = 0

for i in range(1 , 11):
           
        # i = int(input("Enter number including positive negative or zero :" ))
        
        if i == 0:
                zero_counter = zero_counter + 1       
        
        if i > 0 :
                posit_counter = posit_counter + 1
              
        if i < 0 :
                neg_counter = neg_counter + 1
                
# print("Negative",neg_counter)   
print("Zero",zero_counter)
print("Positive",posit_counter)                 

### LEVEL 3: Loops with Conditions

# **Q21. Numbers Divisible by Both 2 and 3**

# Print all numbers from 1 to 100 that are divisible by both 2 and 3.
count = 0
for i in range(1,101):
        if i % 2 == 0 and i % 3 == 0:
                print(i)
                count = count +1
print(count)                
print("Que -- > 21 ends here")
# **Q22. Divisible by 3 but Not by 5**

# Print all numbers from 1 to 100 that are divisible by 3 but not by 5.

for i in range(1 , 101 ):
        if i % 3 == 0 and i % 5 !=0:
                print(i)
print("Que -- > 22 ends here")
                

# **Q23. Numbers Divisible by Neither 2 nor 3*

# Print all numbers from 1 to 100 that are divisible by neither 2 nor 3.

for i in range(1 , 101):
        if i % 3 != 0 and i % 2 != 0 :
                print(i)
                
print("Que -- > 23 ends here")
                
# **Q24. Count Numbers Greater Than 50 and Divisible by 4**
# Count how many numbers from 1 to 100 are greater than 50 and divisible by 4
count = 0
for i in range(1 , 101):
        if i > 50 and i % 4 == 0:
                # print(i)
                count = count + 1
                
print(count)                
print("Que -- > 24 ends here")                
                
# **Q25. Identify Even and Odd Numbers**

# Print numbers from 1 to 50. For each number, display whether it is even or odd.

for i in range(1 , 51):
        if i % 2 == 0:
                
                print("Even : " , i)
        else :
                print("odd :  " , i)

print("Que -- > 25 ends here")
# **Q26. Count Even and Odd Inputs**

# Take 10 numbers from the user. Count how many are even and how many are odd.
Ocount = 0
Ecount = 0 
for i in range(1 , 11):
        num = input("Enter number : ")
        
        if i % 2 == 0:
                print("Even :" , i)
                Ecount = Ecount + 1 
        else :
                print("Odd",i)
                Ocount = Ocount + 1
print(Ecount)
print(Ocount)

print("Que -- > 26 ends here") 
      
# **Q27. Find the Largest Number**

# Take 10 numbers from the user and find the largest number using a `for` loop. Do not use `max()`.

large = 0

for i in range(1 , 10 ):
        num = int(input("Enter number : " ))
        if num > large :
                large = num 
print("Max num is : " , large)

# # **Q28. Find the Smallest Number**

# # Take 10 numbers from the user and find the smallest number using a `for` loop. Do not use `min()`.             
                
small = None

for i in range(1, 11):
    num = int(input("Enter number: "))

    if small is None or num < small:
        small = num

print("Smallest number is:", small)
# # **Q29. Numbers Ending in 5**

# # Print all numbers from 1 to 200 that end with the digit 5.


# for i in range(1 ,201):
#         if i % 5 == 0 :
#                print(i)

# # **Q30. Divisible by 4 or 6, but Not Both**

# # Print all numbers from 1 to 100 that are divisible by 4 or 6, but not both.

# for i in range(1 ,101):
#        if (i % 4 == 0) ^ ( i % 6 == 0 ):
#                print(i)

# # # ### LEVEL 4: Number Digits and Strings

# # # # **Q31. Count Digits**

count = 0 

for i in range(1 , 2):
        num = int(input("Enter number : "))
        if num // 0 :
                # print(i)
                count = count + 1
print(count) 
      
                
num = int(input("Enter a positive integer: "))
count = 0

for i in range(num):
    if num > 0:
        count = count + 1
        num = num // 10
    else:
        break

# # print("Number of digits:", count)

num = 1234 

reverse = 0
for i in range(4):
        digit = num % 10
        reverse=reverse * 10 + digit
        num = num // 10
print (reverse)

num = int(input("Enter number"))

num = 1234 
sum = 0
for i in range(1,5):
        if num % 10 :
           digit = num % 10     
                
           sum = sum + digit
           num = num // 10
print(sum) 

# Question 33 — Product of Digits

# # # Write a Python program to calculate the product of all digits in a positive
# # # integer using a for loop, without converting the number to a string.

num = 1234
mul = 1
for i in range(1,5):
       if num % 10:
        digit = num % 10
        mul = digit * mul
        num = num // 10
# # print(mul)     

# # 34. Reverse a positive integer using a loop, without converting it to a string.

# num = 1234
# reverse = 0

# for i in range(1,5):
#         digit = num % 10 # 4
#         reverse = reverse * 10 + digit
#         num = num // 10 
            
# print(reverse)                

# # 35. Check whether a positive integer is a palindrome using a loop.
num = 12321
original = num
reverse = 0

for i in range(1,6):      
        digit = num % 10
        reverse = reverse * 10 + digit
        num= num // 10
        
if original == reverse:
        print("Palindrome")
else:
        print("Not Palindrome")

print("Reversed number :" , reverse)
        
# 36. Count how many digits in a positive integer are even and how many are odd.
num = 123456789
Ecount = 0
Ocount=0
for i in range(1 , 10):
        digit = num % 10
        if digit % 2 == 0:
                Ecount = Ecount + 1        
        else:
                Ocount = Ocount + 1
                
        num = num // 10
        
print("Even :" , Ecount) 
print("Odd :" , Ocount)       


# # 37. Print each character of a string on a separate line.

str = "Vaishnavi"

for i in range(0,9):
        print(str[i])
       
# # 38. Count the number of vowels in a string.
str = "Vaishnavi"
count = 0
vowels = ("a","e", "i","u", "o")
for i in str:
        if i in vowels :
                count = count + 1
print(count)
                       


# 39. Count the number of uppercase letters, lowercase letters, and digits in a string.
str = "Vaishnavi"
count = 0
Lcount = 0
Ucount =0
vowels = ("a","e", "i","u", "o")

for i in str:
                
        if i.isupper():
                Ucount = Ucount + 1  
                
        elif i.islower():
                Lcount = Lcount + 1             

print("Lower " , Lcount)
print("Upper " , Ucount)
            


# # # 40. Reverse a string using a loop, without using slicing.

name = "Vaishnavi"

for i in range(8, 0, -1):
    print(name[i], end="")
        

# # # ## Level 5: Advanced Beginner — Prepare for Your Teacher's Challenge

# # # **Goal:** Apply multiple concepts and develop independent problem-solving skills.

# # # 41. Ask the user for a positive integer and check whether it is prime.


num = 7

for i in range(2 , num):
        if num % 2 == 0:
                print("Not prime")
else:
                print("Prime hai bhaiii")        

# # # 42. Print all prime numbers between 1 and 100.

for i in range(1 ,101):
        if i % 2 != 0:
             print("Prime", i)

# # # 43. Find the factorial of a positive integer using a loop.

fact = int(input("Enter Number : "))

for i in range( 1 , fact):
        fact = fact * i
print(fact)

# # 44. Print the Fibonacci sequence for the first `n` terms, where `n` is entered by the user.

n = int(input("Enter Number"))

a = 0
b = 1 

for i in range(n):
        print(a)
        c = a + b # 0+1 = 1
        a = b #1
        b = c
# a = 1 , b = 1


# Question 45 — Reverse a Number

# Write a Python program to reverse a given number using a for loop.

num = 1234
reverse = 0
for i in range(5):

        reverse = reverse * 10 + num % 10  
       
        num = num // 10
print(reverse)       
# #  # # # 45. Find the greatest common divisor (GCD) of two positive integers using a loop.
 
 
a = 18 
b = 12
gdc = 0

for i in range(1 , 13):
        if a % i == 0 and b % i == 0 :
                gcd = i
print(gcd)                
                
 
 
 
# 46. Check whether a positive integer is an Armstrong number.


num = 153
original = num
length = len(str(num))
total = 0

for i in range(length):
    digit = num % 10
    total = total + digit ** length
    num = num // 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

# # # # 47. Print the following pattern for `n = 5`:

    
for j in range(1,6):
        for i in range(0,j):
                print("*", end=" ")

        print("  ")   

# # # # 48. Print the following number pattern for `n = 5`:


n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print() 
    
# # # # 49. Find the second-largest distinct number in a list without using `sort()` or `max()`.

numbers = [10, 5, 20, 8, 20, 15]

largest = float('-inf')
second_largest = float('-inf')

for i in numbers:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

if second_largest == float('-inf'):
    print("Second-largest distinct number does not exist")
else:
    print("Second-largest distinct number:", second_largest)


# # # # 50. Ask the user for a positive integer and determine whether it is a perfect number.


num = int(input("Enter a positive integer: "))
total = 0

for i in range(1, num):
    if num % i == 0:
        total = total + i

if num > 0 and total == num:
    print("Perfect number")
else:
    print("Not a perfect number")
