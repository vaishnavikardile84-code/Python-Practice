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
# # name = "Abhishek"

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
# total = 0
# for i in range(1 , 11):
#     total = total + i

# print(total)  


# # # 18. Reverse a string using a `for` loop without using slicing.
# name = "vaishnavi"

# for chr in reversed(name) :
#     print(chr)
  