# <<<<<<< HEAD
# # # ## Level 1: Beginner — Understand the `while` Loop


# # # # 1. Print numbers from **1 to 10** using a `while` loop.

# # # i = 1
# # # while i <= 10:
# # #     print(i)
# # #     i+=1

# # # # 2. Print numbers from **10 to 1** in reverse order.
# # # i = 10
# # # while i >= 1:
# # #     print(i)
# # #     i=i-1
# # # # 3. Print all even numbers from **2 to 50**.

# # # i = 2
# # # while i <= 50 :
# # #     if i % 2 == 0 :
# # #         print(i)
# # #     i = i+1
    
# # # # 4. Print all odd numbers from **1 to 49**.

# # # i = 1 
# # # while i <= 49:
# # #     if i % 2 != 0 :
# # #         print(i)
# # #     i = i+1    

# # ## 5. Print the multiplication table of a number entered by the user.

# # # num = int(input("Enter a number: "))

# # # i = 1
# # # while i <= 10:
       
# # #     print(num * i)
# # #     i+=1
# # # #6. Print the squares of numbers from **1 to 10**.

# # # i = 1
# # # while i <= 10:
# # #     print(i*i)
# # #     i += 1
    

# # # # 7. Print the cubes of numbers from **1 to 10**.

# # # i = 1
# # # while i <= 10:
# # #     print(i * i * i )
# # #     i=i+1
    
# # # 8. Print numbers from **1 to 100** that are divisible by 5.

# # # i = 1
# # # while i <= 100:
# # #     if (i % 5 == 0):
# # #         print(i)
    
# # #     i = i+1
      
# # # # 9. Print numbers from **50 to 1**, decreasing by 5 each time.

# # # i = 50
# # # while i >= 1:
# # #     if i % 5 == 0:
# # #         print(i)
# # #     i=i-1

# # # 10. Print the first 10 positive integers and their corresponding squares.

# # # i =1
# # # while i <= 10:
# # #     sq = i * i
# # #     print(sq)
        
# # #     i = i+1    

# # # ## Level 2: Basic Logic Building

# # # **Questions 11–20**

# # # 11. Calculate the sum of numbers from **1 to N**, where N is entered by the user.

# # # n = int(input("Enter Number : "))
# # # sum = 0
# # # i = 1

# # # while i <= n:
# # #     sum = sum + i
# # #     i = i+1
# # # print(sum)  

  
# # # 12. Calculate the sum of all even numbers from **1 to N**.

# # # n = int(input("Enter number : "))

# # # sum = 0
# # # i = 1
# # # while i <= n:
# # #     if (i % 2 == 0):
# # #         sum =  sum + i 
# # #     i = i+1
# # # print(sum)    


# # # # 13. Calculate the sum of all odd numbers from **1 to N**.

# # # n = int(input("Enter input"))

# # # sum = 0

# # # i = 1

# # # while i <= n:
# # #     if i % 2 != 0:
# # #         sum = sum + i
# # #     i = i+1
# # # print(sum)
        

# # # # 14. Calculate the factorial of a number entered by the user.

# # # n = int(input("Enter Number : "))
# # # fact = 1
# # # i = 1
# # # while i <= n :
# # #     fact = fact * i
# # #     i +=1
# # # print(fact)   

# # # 15. Count how many numbers are divisible by both 3 and 5 
# # # between **1 and 100**.

# # # i = 1
# # # count = 0
# # # while i <= 100:
# # #     if i % 3 == 0 and i % 5 == 0:
# # #         count = count + 1
# # #     i +=1
# # # print(count)

# # # # 16. Calculate the product of numbers from **1 to N**.

# # # n = int(input("Enter number : "))
# # # product = 1
# # # i = 1
# # # while i <= n:
# # #     product = product * i
    
# # #     i = i+1
# # # print(product)        
        
    

# # # 17. Find the average of numbers from **1 to N**.

# # n = int(input("Enter number : "))

# # avg = 0
# # sum = 0
# # count = 0
# # i = 1

# # while i <= n:
    
# #     sum = sum + i
# #     count = count + 1
# #     i = i+1
# # avg = sum / count
    
# # print(avg)   


# # # 18. Print the first N multiples of a number entered by the user.

# # n = int(input("Enter Number a : "))

# # i = 1
# # while i <= n:
# #     n * i
    
    

# # # 19. Calculate the sum of squares from **1 to N**.
# =======
# ## Level 1: Beginner — Understand the `while` Loop


# # 1. Print numbers from **1 to 10** using a `while` loop.

# i = 1
# while i <= 10:
#     print(i)
#     i+=1

# # 2. Print numbers from **10 to 1** in reverse order.
# i = 10
# while i >= 1:
#     print(i)
#     i=i-1
# # 3. Print all even numbers from **2 to 50**.

# i = 2
# while i <= 50 :
#     if i % 2 == 0 :
#         print(i)
#     i = i+1
    
# # 4. Print all odd numbers from **1 to 49**.

# i = 1 
# while i <= 49:
#     if i % 2 != 0 :
#         print(i)
#     i = i+1    

# # 5. Print the multiplication table of a number entered by the user.

# num = int(input("Enter a number: "))

# i = 1
# while i <= 10:
       
#     print(num * i)
#     i+=1
# #6. Print the squares of numbers from **1 to 10**.

# i = 1
# while i <= 10:
#     print(i*i)
#     i += 1
    

# # 7. Print the cubes of numbers from **1 to 10**.

# i = 1
# while i <= 10:
#     print(i * i * i )
#     i=i+1
    
# # 8. Print numbers from **1 to 100** that are divisible by 5.

# i = 1
# while i <= 100:
#     if (i % 5 == 0):
#         print(i)
    
#     i = i+1
      
# # 9. Print numbers from **50 to 1**, decreasing by 5 each time.

# i = 50
# while i >= 1:
#     if i % 5 == 0:
#         print(i)
#     i=i-1

# # 10. Print the first 10 positive integers and their corresponding squares.

# i =1
# while i <= 10:
#     sq = i * i
#     print(sq)
        
#     i = i+1    

# ## Level 2: Basic Logic Building

# # **Questions 11–20**

# # 11. Calculate the sum of numbers from **1 to N**, where N is entered by the user.

# n = int(input("Enter Number : "))
# sum = 0
# i = 1

# while i <= n:
#     sum = sum + i
#     i = i+1
# print(sum)  

  
# # 12. Calculate the sum of all even numbers from **1 to N**.

# n = int(input("Enter number : "))

# sum = 0
# i = 1
# while i <= n:
#     if (i % 2 == 0):
#         sum =  sum + i 
#     i = i+1
# print(sum)    


# # 13. Calculate the sum of all odd numbers from **1 to N**.

# n = int(input("Enter input"))

# sum = 0

# i = 1

# while i <= n:
#     if i % 2 != 0:
#         sum = sum + i
#     i = i+1
# print(sum)
        

# # 14. Calculate the factorial of a number entered by the user.

# n = int(input("Enter Number : "))
# fact = 1
# i = 1
# while i <= n :
#     fact = fact * i
#     i +=1
# print(fact)   

# # 15. Count how many numbers are divisible by both 3 and 5 
# # between **1 and 100**.

# i = 1
# count = 0
# while i <= 100:
#     if i % 3 == 0 and i % 5 == 0:
#         count = count + 1
#     i +=1
# print(count)

# # 16. Calculate the product of numbers from **1 to N**.

# n = int(input("Enter number : "))
# product = 1
# i = 1
# while i <= n:
#     product = product * i
    
#     i = i+1
# print(product)        
        
    

# # 17. Find the average of numbers from **1 to N**.

# n = int(input("Enter number : "))

# avg = 0
# sum = 0
# count = 0
# i = 1

# while i <= n:
    
#     sum = sum + i
#     count = count + 1
#     i = i+1
# avg = sum / count
    
# print(avg)   


# # 18. Print the first N multiples of a number entered by the user.

# n = int(input("Enter Number a : "))

# i = 1
# while i <= n:
#     n * i
    
    

# # 19. Calculate the sum of squares from **1 to N**.
# >>>>>>> 045555b (Added Python practice files)

# n=5
# sum  = 0
# i = 1
# while i <= n:
   
#     sum = sum + (i  ** 2)
#     i +=1
# print(sum)    
    

# # # 20. Print the following pattern using a `while` loop:
# n = 5

# i = 1

# while i <= n:
#     print("*" * i)
    
#     i = i+ 1

# # #     ```text
# # #     *
# # #     **
# # #     ***
# # #     ****
# # #     *****
# # #     ```

# <<<<<<< HEAD
# # # ## Level 3: Number Logic and Digit Manipulation

# # # **Questions 21–30**

# # # # 21. Count the number of digits in a positive integer.

# # n = 1234
# # count = 0

# # i = 1

# # while n > 0 :
# #     n = n // 10
# #     count = count + 1 
# #     i += 1
# # print(count)



# # # # 22. Calculate the sum of all digits of a number.

# # n = 1234
# # sum = 0

# # i = 1
# # while n > 0:
# #     digit = n % 10
# #     sum = sum + digit
# #     n = n // 10
# #     i = i+1
# # print(sum)    
# =======
# # ## Level 3: Number Logic and Digit Manipulation

# # **Questions 21–30**

# # # 21. Count the number of digits in a positive integer.

# n = 1234
# count = 0

# i = 1

# while n > 0 :
#     n = n // 10
#     count = count + 1 
#     i += 1
# print(count)



# # # 22. Calculate the sum of all digits of a number.

# n = 1234
# sum = 0

# i = 1
# while n > 0:
#     digit = n % 10
#     sum = sum + digit
#     n = n // 10
#     i = i+1
# print(sum)    
# >>>>>>> 045555b (Added Python practice files)
    


# # # 23. Calculate the product of all digits of a number.

# n = 1234
# product = 1
# i = 1
# while n > 0:
#     digit = n % 10
#     product = product * digit
    
#     n = n // 10

# print(product)

# # # 24. Reverse a number. For example, `1234` becomes `4321`.

# a = 1234 

# i = 1
# reverse = 0

# while a > 0 :
    
#     digit = a % 10 
#     reverse = reverse * 10 + digit
    
#     i = i+1
#     a = a // 10
    
# print(reverse)    
     
    

# # # 25. Check whether a number is a palindrome. For example, `121` is a palindrome.


# a = 1234 

# original = a

# i = 1
# reverse = 0

# while a > 0 :
    
#     digit = a % 10 
#     reverse = reverse * 10 + digit
    
#     i = i+1
#     a = a // 10
    
# print(reverse) 


# if original == reverse:
#     print("Palindrome")
# else:
#     print("Not palindrome")
# <<<<<<< HEAD
# =======
    

# # # 26. Find the largest digit in a number.

# num = int(input("Enter num : "))

# large = 0

# i = 1
# while num >0:
#     digit =  num % 10
#     if digit > large :
#         large = digit
#     num = num // 10
# print(large)        
        
    
   
    
# # # # 27. Find the smallest digit in a number.

# num = 123456

# small = 1

# i = 1
# while num>0:
#     digit = num % 10
#     if digit < small :
#         small = digit
#     num = num // 10
# print(small)        
    

# # # 28. Count how many digits in a number are even and how many are odd.

# num = 1234567890

# i = 1
# even = 0
# odd = 0

# while i <= 1:

#     if num % 2 == 0:
        
#         even += 1
        
#     else:
    
#         odd += 1 
#     i = i +1     
# print(odd)
# print(even)        
         

# # # # 29. Check whether a number is an Armstrong number.



# # # # 30. Check whether a number is a perfect number.

# # # # ## Level 4: Intermediate — Conditions and Repeated Calculations

# # # # **Questions 31–40**

# # # # 31. Check whether a number is prime.
# # # # 32. Print all prime numbers between **1 and N**.
# # # # 33. Find the GCD of two positive integers using a `while` loop.
# # # # 34. Find the LCM of two positive integers using a `while` loop.
# # # # 35. Generate the Fibonacci sequence for N terms.
# # # # 36. Find the first Fibonacci number greater than a number entered by the user.
# # # # 37. Calculate the sum of the series `1 + 2 + 3 + ... + N` without using a formula.
# # # # 38. Keep accepting numbers from the user until they enter `0`, then display the sum of all previously entered numbers.
# # # # 39. Keep accepting numbers until the user enters a negative number, then display how many positive numbers were entered.
# # # # 40. Create a number-guessing program that continues until the user guesses the secret number correctly.

# # # # ## Level 5: Advanced Logic Building

# # # # **Questions 41–50**

# # # # 41. Check whether a number is a **strong number**. A strong number equals the sum of the factorials of its digits. For example, `145 = 1! + 4! + 5!`.

# # # # 42. Check whether a number is a **Harshad number**. A Harshad number is divisible by the sum of its digits.

# # # # 43. Check whether a number is a **perfect square** without using square-root functions.

# # # # 44. Find the second-largest digit in a number without using `sort()` or `max()`.

# # # # 45. Convert a positive decimal integer to binary using a `while` loop.

# # # # 46. Find the HCF of the digits of a positive integer.

# # # # 47. Print this number pattern using a `while` loop:

# # # #     ```text
# # # #     1
# # # #     12
# # # #     123
# # # #     1234
# # # #     12345
# # # #     ```

# # # # 48. Print this pattern using a `while` loop:

# # # #     ```text
# # # #     5
# # # #     54
# # # #     543
# # # #     5432
# # # #     54321
# # # #     ```

# # # # 49. Find the first number greater than 100 that is divisible by both 7 and 9.

# # # # 50. Write a menu-driven calculator that repeatedly asks the user to choose addition, subtraction, multiplication, or division. Continue until the user selects Exit.    
# >>>>>>> 045555b (Added Python practice files)

