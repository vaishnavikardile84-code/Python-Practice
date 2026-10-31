# Create a tuple containing five integers and print it.
num =(11,13,78,65,77)

for index in num:
    print(index)
    
i = 0
while i < len(num):
    print(num[i])
    i+=1    

# 2. Create a tuple containing a string, integer, float, and Boolean value.
data = ("vaishn" , 21 , "mca" , 60.23, True)

information= 0
while information < len(data):
    print(data[information])
    information +=1
    
for i in range(len(data)):
    print(data[i])    
    

# 3. Create a single-element tuple and verify its datatype.
A = (10,)
print(type(A))

# 4. Print the first, middle, and last elements of a tuple.
A = (12,45,32,12,34,5,90)

first , *middle , last = A
print(first)
print(middle) #list
print(last)    

# # 5. Reverse a tuple using slicing.
A = (12,45,32,12,34,5,90)

reverse = A[::-1]
print(reverse)


# 6. Print every second element using slicing.

A = (12,45,32,12,34,5,90)

reverse = A[1:6:2]
print(reverse)

# Intermediate Level

# 7. Count how many times 25 occurs in a tuple.

A = (12,25,32,12, 20 , 25 ,34,5,90)

print(A.count(25))


# 8. Find the index of a given element.
A = (12,25,32,12, 20 , 25 ,34,5,90)

print(A.index(25))

# 9. Calculate the sum and average of numeric tuple elements.
A = (12,25,32,12, 20 , 25 ,34,5,90)
sum = 0
count = 0
for i in range(len(A)):
    sum += A[i]
    count+=1
    avg = sum / count
print(avg)
print(sum)    
# 10. Count even and odd numbers in a tuple.
A = (12,25,32,12, 20 , 25 ,34,5,90)
even = 0
odd = 0

i = 0
while i < len(A):
    if A[i] % 2 == 0 :
        even+=1
    else:
        odd+=1
    i+=1
print(even)
print(odd)        

# 11. Find the maximum and minimum values.

print(max(A))
print(min(A))


# 12. Check whether a particular value exists in a tuple.
A = (12,25,32,12, 20 , 25 ,34,5,90)

if 25 in A:
        print(True)
        
# B = list[A]
# B.append(A)

# temp = B

# print(temp)
     
B= []
B.append(A)
print(B)   
print(type(B))  

# 13. Convert a list into a tuple.
data = ["vaishn" , 21 , "mca" , 60.23, True]

tup = tuple(data)
print(tup)
print(type(tup))


# 14. Unpack a tuple into four variables.

var = ("Vaish" , "Rani " , 23, 11.2 , "god" )

First , *middle , Last = var

print("last ele ",Last)
print("First ele",First)
print("Middle",*middle)
# 15. Swap two variables using tuple unpacking.

a = 10 
b = 36
print(a , b)
a , b = b , a

print(a , b)

# Advanced Level

# 16. Access a specific value from a nested tuple.

tup = (12,34,56,[12,98,65,43] , 47 ,43,67)

print(tup[3][2])

# # 17. Remove duplicate values while preserving order.
A = (12, 25, 32, 12, 20 , 25 ,34, 5, 90 )

new_list = []


for i in range(len(A)): 
    if (A[i]) not in new_list:
        
        new_list.append(A[i])
print(new_list)
# # # 18. Find the second-largest distinct number.
A = (12, 25, 32, 12, 20 , 25 ,34, 5, 90 )

distinct = []

for i in range(len(A)): 
    if (A[i]) not in distinct:
        
        distinct.append(A[i])
largest = max(distinct)   
distinct.remove(largest)
second_largest = max(distinct)
print(second_largest)

# # 19. Sort a tuple in ascending
# order and convert the result back into a tuple.
A = (12, 25, 32, 12, 20 , 25 ,34, 5, 90 )
B = list(A)
print(B)
B.sort()
print(B)
B = tuple(B)
print(B)

# # 20. Create a tuple of student names
# and marks, then print each student's details.

students = (("Aarav", 85),("Priya", 92),("Rohan", 78),("Sneha", 90))

for i in range(len(students)):
    print("Name:", students[i][0])
    print("Marks:", students[i][1])
    print("----------------")