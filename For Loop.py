# # ## Level 1: Basic — Understand the `for` Loop

# # ##1. Print numbers from 1 to 10 using a `for` loop.

# for i in range(1 , 11):
#     print(i)

# # # #2. Print numbers from 10 to 1 in reverse order.

# for i in range (11 ,0 , -1):
#     print(i)

# # ## 3. Print all even numbers from 1 to 50.

# # for i in range(0 , 51 , 2):
# #     print(i)

# for i in range(0 , 51 ,2):
#     print(i)
    
    
# # #4. Print all odd numbers from 1 to 50.

# for i in range(1 , 51 , 2):
#     print(i)

# # #  #5. Print each character of a string on a separate line.
# name = "vaish"
# for chr in name:
#     print(chr)

# name = "Krishna"
# for chr in name:
#     print(chr)


# # # # 6. Print each element of a list using a `for` loop.

# lst = ["pen" , "paper" , "rubber" , "pencil"]
# for i in lst:
#     print(i)
    
    
    
# name = "Abhishek"

# for i in name :
#     print(i)
#     if(i == "b"):
#         print("This is very easy")    


    
# # # # 7. Calculate the sum of numbers from 1 to 10.

# total = 0
# for i in range(0 , 11):
#     total = total + i
#     print(total)



# # # # 8. Print the multiplication table of a number entered by the user.
# num = int(input("Enter Number : "))

# for i in range (0 , 10 ,2):
#     print(num * i)
    
    

# num = int(input("Enter Number: "))

# for i in range(1, 11):
#     print(num, "X", i, "=", num * i)

# # # 9. Count how many characters are present in a string without using `len()`.

# str = "vaish"

# for chr in range(0,5):
#     print(str[chr])

# # # # 10. Print the squares of numbers from 1 to 10.

# for i in range (1 , 11 ):
#     print(i  ** 2)


# # # # ## Level 2: Basic Logic Building

# # # # 11. Calculate the sum of all even numbers from 1 to 100.

# for i in range ( 0 , 101):
#     if(i % 2 == 0):
#         print(i)
     
# # # 12. Calculate the sum of all odd numbers from 1 to 100.
# total = 0
# for i in range ( 1 , 101):
#     if(i % 2 == 1):
        
#         total = (i + total)
     
# print( total)        
        

# # # 13. Count how many vowels are present in a string.

# vowels = "vaishnavi"
# for i in vowels :
#     print(i)
#     if i in "aeiou" :
#         print("vowels")
#     else:
#         # print("consonant")    
    

# # # example from harry
# name = "Abhishek"

# for i in name :
#     print(i)
#     if (i == "b"):
#         print("This is very easy")   

# colors = ["Red" , "Green" , "Yellow"]

# for colour in colors :
#     print(colour)  
#     for i in colour:
#         print(i)      
        
# name = "Krishna"
# for chr in name:
#     print(chr)        
    

# # 14. Count the number of digits in a number using a loop.
# total = 0
# phone = 987654325

# for i in range(0 , 10):
#     print (i)
#     total = total + i
    
    
# total = 0
# phone = 987654325

# for i in str(phone):
#     total = total + 1

# print("Total digits:", total)    
    

# # 15. Calculate the factorial of a number.


# total = 1

# for i in range(4 , 0 ,-1):
   
    
#     total = total * i
    
# print(total)


# # 16. Print all numbers between 1 and 100 that are divisible by both 3 and 5.

# for i in range(1 , 101):
#     if i % 3 == 0 and i % 5 == 0 :
#         print(i)

# # 17. Find the sum of the digits of a number.
total = 0
for i in range(1 , 11):
    total = total + i

print(total)  


# # 18. Reverse a string using a `for` loop without using slicing.
name = "vaishnavi"

for chr in reversed(name) :
    print(chr)
    
# # 19. Find the largest number in a list without using `max()`.

# total = 0
numbers = [23, 56, 12, 89, 34, 7, 65, 91, 45, 18]


# for i in numbers :
#     largest = max(numbers)
#         # print(i)
        
# print(largest)

largest = numbers[0]

for i in numbers :
    if i > largest:
        largest = i
print(largest)    


# # 20. Find the smallest number in a list without using `min()`.

# # # ## Level 3: Intermediate — Conditions and Logic

# # # 21. Check whether a number is prime using a `for` loop.
# # # 22. Print all prime numbers between 1 and 100.
# # # 23. Check whether a number is a palindrome using a loop.
# # # 24. Check whether a number is an Armstrong number.
# # # 25. Print the Fibonacci sequence up to `n` terms.
# # # 26. Count how many positive, negative, and zero values are present in a list.
# # # 27. Find the second-largest number in a list without using `sort()` or `max()`.
# # # 28. Calculate the sum of all elements in a list without using `sum()`.
# # # 29. Count how many times a given element appears in a list without using `count()`.
# # # 30. Create a new list containing only the even numbers from an existing list.

# # # ## Level 4: Nested Loops and Patterns

# # # 31. Print this pattern:

# # # ```text
# # # *
# # # **
# # # ***
# # # ****
# # # *****
# # # ```

# # # 32. Print this pattern:

# # # ```text
# # # *****
# # # ****
# # # ***
# # # **
# # # *
# # # ```

# # # 33. Print this number pattern:

# # # ```text
# # # 1
# # # 12
# # # 123
# # # 1234
# # # 12345
# # # ```

# # # 34. Print this pattern:

# # # ```text
# # # 1
# # # 22
# # # 333
# # # 4444
# # # 55555
# # # ```

# # # 35. Print this pattern:

# # # ```text
# # #     *
# # #    ***
# # #   *****
# # #  *******
# # # *********
# # # ```

# # # 36. Print a rectangle of stars with 4 rows and 6 columns.
# # # 37. Print a multiplication table from 1 to 10 using nested `for` loops.
# # # 38. Print this pattern:

# # # ```text
# # # 1
# # # 23
# # # 456
# # # 78910
# # # ```

# # # 39. Print a right-aligned triangle of stars with 5 rows.
# # # 40. Print a pyramid of numbers where each row contains the row number repeated that many times, centered like a pyramid.

# # # ## Level 5: Advanced — Real Logic Challenges

# # # 41. Find all pairs of numbers in a list whose sum equals a target number.
# # # 42. Find the common elements between two lists without using sets.
# # # 43. Remove duplicate elements from a list using a `for` loop without converting it to a set.
# # # 44. Find the frequency of every element in a list without using `count()` or importing any library.
# # # 45. Find all the numbers between 1 and 1000 that are divisible by the sum of their digits.
# # # 46. Check whether a number is a perfect number. A perfect number equals the sum of its positive divisors, excluding itself.
# # # 47. Find all Armstrong numbers between 1 and 10,000.
# # # 48. Rotate a list to the right by one position using a loop, without using slicing.
# # # 49. Find the longest word in a sentence without using `max()` or `sorted()`.
# # # 50. Given a list of student marks, calculate the class average, find the highest and lowest marks, and count how many students passed (marks ≥ 35), using `for` loops without using `sum()`, `max()`, or `min()`.
    