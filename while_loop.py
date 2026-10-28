# # ## Level 1: Beginner — Understand the `while` Loop


# # # 1. Print numbers from **1 to 10** using a `while` loop.

# # i = 1
# # while i <= 10:
# #     print(i)
# #     i+=1

# # # 2. Print numbers from **10 to 1** in reverse order.
# # i = 10
# # while i >= 1:
# #     print(i)
# #     i=i-1
# # # 3. Print all even numbers from **2 to 50**.

# # i = 2
# # while i <= 50 :
# #     if i % 2 == 0 :
# #         print(i)
# #     i = i+1
    
# # # 4. Print all odd numbers from **1 to 49**.

# # i = 1 
# # while i <= 49:
# #     if i % 2 != 0 :
# #         print(i)
# #     i = i+1    

# ## 5. Print the multiplication table of a number entered by the user.

# # num = int(input("Enter a number: "))

# # i = 1
# # while i <= 10:
       
# #     print(num * i)
# #     i+=1
# # #6. Print the squares of numbers from **1 to 10**.

# # i = 1
# # while i <= 10:
# #     print(i*i)
# #     i += 1
    

# # # 7. Print the cubes of numbers from **1 to 10**.

# # i = 1
# # while i <= 10:
# #     print(i * i * i )
# #     i=i+1
    
# # 8. Print numbers from **1 to 100** that are divisible by 5.

# # i = 1
# # while i <= 100:
# #     if (i % 5 == 0):
# #         print(i)
    
# #     i = i+1
      
# # # 9. Print numbers from **50 to 1**, decreasing by 5 each time.

# # i = 50
# # while i >= 1:
# #     if i % 5 == 0:
# #         print(i)
# #     i=i-1

# # 10. Print the first 10 positive integers and their corresponding squares.

# # i =1
# # while i <= 10:
# #     sq = i * i
# #     print(sq)
        
# #     i = i+1    

# # ## Level 2: Basic Logic Building

# # **Questions 11–20**

# # 11. Calculate the sum of numbers from **1 to N**, where N is entered by the user.

# # n = int(input("Enter Number : "))
# # sum = 0
# # i = 1

# # while i <= n:
# #     sum = sum + i
# #     i = i+1
# # print(sum)  

  
# # 12. Calculate the sum of all even numbers from **1 to N**.

# # n = int(input("Enter number : "))

# # sum = 0
# # i = 1
# # while i <= n:
# #     if (i % 2 == 0):
# #         sum =  sum + i 
# #     i = i+1
# # print(sum)    


# # # 13. Calculate the sum of all odd numbers from **1 to N**.

# # n = int(input("Enter input"))

# # sum = 0

# # i = 1

# # while i <= n:
# #     if i % 2 != 0:
# #         sum = sum + i
# #     i = i+1
# # print(sum)
        

# # # 14. Calculate the factorial of a number entered by the user.

# # n = int(input("Enter Number : "))
# # fact = 1
# # i = 1
# # while i <= n :
# #     fact = fact * i
# #     i +=1
# # print(fact)   

# # 15. Count how many numbers are divisible by both 3 and 5 
# # between **1 and 100**.

# # i = 1
# # count = 0
# # while i <= 100:
# #     if i % 3 == 0 and i % 5 == 0:
# #         count = count + 1
# #     i +=1
# # print(count)

# # # 16. Calculate the product of numbers from **1 to N**.

# # n = int(input("Enter number : "))
# # product = 1
# # i = 1
# # while i <= n:
# #     product = product * i
    
# #     i = i+1
# # print(product)        
        
    

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

n=5
sum  = 0
i = 1
while i <= n:
   
    sum = sum + (i  ** 2)
    i +=1
print(sum)    
    

# # 20. Print the following pattern using a `while` loop:
n = 5

i = 1

while i <= n:
    print("*" * i)
    
    i = i+ 1

# #     ```text
# #     *
# #     **
# #     ***
# #     ****
# #     *****
# #     ```

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
    


# # 23. Calculate the product of all digits of a number.

n = 1234
product = 1
i = 1
while n > 0:
    digit = n % 10
    product = product * digit
    
    n = n // 10

print(product)

# # 24. Reverse a number. For example, `1234` becomes `4321`.

a = 1234 

i = 1
reverse = 0

while a > 0 :
    
    digit = a % 10 
    reverse = reverse * 10 + digit
    
    i = i+1
    a = a // 10
    
print(reverse)    
     
    

# # 25. Check whether a number is a palindrome. For example, `121` is a palindrome.


a = 1234 

original = a

i = 1
reverse = 0

while a > 0 :
    
    digit = a % 10 
    reverse = reverse * 10 + digit
    
    i = i+1
    a = a // 10
    
print(reverse) 


if original == reverse:
    print("Palindrome")
else:
    print("Not palindrome")

