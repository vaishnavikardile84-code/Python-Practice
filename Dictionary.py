# Q1. Create a dictionary containing your personal details:
# name, age, , city and percentage.
# Print the complete dictionary.

details = {"name" : "vaish" , "course" : "MCA" ,"age" : 21 , "city" : "Pune" , "percentage" : 95}

print(details)

# Q2. Create a dictionary containing 5 student names as keys
# and their marks as values.
# Print the dictionary and check its datatype.

students_data = { "Virat" : 99,
                 "Surya" : 98,
                 "Hardik" : 89,
                 "Sachin" : 100,
                 "Rohit" : 90
                }
print(students_data)
print(type(students_data))

# # Q3. Access a specific value from a dictionary using its key.
# # Print the student's marks using the student's name.


print(students_data)

print(students_data.get("Virat"))


# Q4. Create a dictionary containing different datatypes:
# string, integer, float, boolean and list.
# Print each value separately.

emp = {"emp_id" : 123 , "name" : "vaish" , "Salary" : 5500.00 ,
       "Is_active" : True,
       "dpt" : ["department" , "it"] }
print(emp.items()) 


# Q5. Create a dictionary with one key and multiple values.
# Access the second value from the collection stored in that key.

Teacher = {"student" : ["Vaishnavi" , "Ranii" ,"Rohit" , "Diksha"]}

print(Teacher.get("student"))

# Q6. Add a new key-value pair.


Emp_data = {"emp_id" : [2135,2136,2136] , "name" : ["vaish", "rani","sani"] ,"department" : ["IT","Finance","Sales" ] }

Emp_data.update({"Salary": [45000, 5000 , 45000]}) 

print(Emp_data)
 
# Q7. Update an Existing Value.

# Create a dictionary containing 5 student names and their marks.

stud = {"Name" : ["vaish" , "rani" , "om" ,"shree" ,"odh"],"marks" : [98,88,99,76,767]}

# Update the marks of one existing student.

stud["marks"] [1] =70
stud["marks"] [1]= 30

# # Print the updated dictionary.
print(stud)
# # Q8. Remove an Item Using pop().

# # Create a dictionary containing employee names and their salaries.
Emp_data = {"emp_id" : [2135,2136,2136] , "name" : ["vaish", "rani","sani"] ,"department" : ["IT","Finance","Sales" ] }
# print(Emp_data)

Emp_data.pop("name")
print(Emp_data)




# # Print the dictionary before and after removal.

# # Q9. Remove the Last Inserted Item Using popitem().

# # Create a dictionary containing 4 products and their prices.

products = {"pname" : ["laptop" , "mobile" , "tripod" ,"ipad"],"price" : [45000,34000,45000,20000]}

# # Print the dictionary before and after using popitem().
print(products)

# # Q10. Demonstrate Dictionary Methods.]
removed_items = products.popitem()
products.popitem() 
print("Removed item:", removed_items)
print(products)

# # Create a dictionary and demonstrate the following methods:

# # keys(), values(), items(), get() and update().

# # Print the result of each operation.
stud = {"Name" : ["vaish" , "rani" , "om" ,"shree" ,"odh"],"marks" : [98,88,99,76,767]}

print(stud.keys())
print(stud.values())
print(stud.items())
print(stud.get("marks"))
print(stud.update({"name" : "krishn"}))
print(stud)

# # ============================================================

# # LEVEL 3: LOOPS AND LOGIC BUILDING

# # ============================================================

# # Q11. Print All Keys.

# # Create a dictionary containing 5 countries and their capitals.
stud = {"Name" : ["vaish" , "rani" , "om" ,"shree" ,"odh"],"marks" : [98,88,99,76,767]}

# # Use a for loop to print all the keys.

for i in stud:
       print(i)

# # Q12. Print All Values.

for i in stud.values():
       print(i)

# # Create a dictionary containing 5 products and their prices.

# # Use a for loop to print all the values.

products = {"pname" : ["laptop" , "mobile" , "tripod" ,"ipad"],"price" : [45000,34000,45000,20000]}

for i in products.items():
       print(i)

# # Q13. Print Keys and Values.

# # Create a dictionary containing 5 employees and their departments.
Emp_data = {"emp_id" : [2135,2136,2136] , "name" : ["vaish", "rani","sani"] ,"department" : ["IT","Finance","Sales" ] }


# # Use a for loop and items() to print each employee's name

for key , values in Emp_data.items():
       print(key ,values)
       
       for i in range(len(Emp_data["name"])):
              print("Name:", Emp_data["name"][i], "Department:", Emp_data["department"][i])

# # along with their department.

# # Q14. Calculate the Sum of Values.


# # Create a dictionary containing 5 products and their prices.
products = {"pname" : ["laptop" , "mobile" , "tripod" ,"ipad"],"price" : [45000,34000,45000,20000]}

total = 0
# # Calculate and print the total of all prices using a loop.
for i in  products["price"]:
       total = total + i
print(total)
       
# # Q15. Count Students Scoring Above 60.

# # Create a dictionary containing 6 student names and their marks.
stud = {"Name" : ["vaish" , "rani" , "om" ,"shree" ,"odh"],"marks" : [98,88, 60 , 61,99,76,77 ,67]}


# # Count how many students scored more than 60.
count = 0
for i in stud["marks"]:
       if i > 60:
              count=count+1
print(count)    

print(max("marks"))      
print(max(stud["marks"]))    
              

# # Print the count.

# # ============================================================

# # LEVEL 4: INTERMEDIATE PROBLEM SOLVING

# # ============================================================

# # Q16. Find the Student with the Highest Marks.

print(max(stud["marks"]))   

# # Create a dictionary containing student names and marks.

# # Find and print the name of the student with the highest marks.


print(stud["marks"].index(max(stud["marks"])))
# # Q17. Find the Student with the Lowest Marks.

# # Create a dictionary containing student names and marks.

# # Find and print the name of the student with the lowest marks.

# # Q18. Character Frequency.

# # Given the string "programming", count how many times each

# # character appears using a dictionary.

# # Print the resulting dictionary.

# # Q19. Merge Two Dictionaries.

# # Create two dictionaries containing product names and prices.

# # Merge them into one dictionary.

# # Include at least one key that appears in both dictionaries.

# # Observe which value is retained for the duplicate key.

# # Print the merged dictionary.

# # Q20. Create a Filtered Dictionary.

# # Create a dictionary containing student names and marks.

# # Create a NEW dictionary containing only students whose marks

# # are greater than 50.

# # Print the new dictionary without modifying the original.

# # ============================================================

# # LEVEL 5: ADVANCED AND REAL-WORLD APPLICATIONS

# # ============================================================

# # Q21. Nested Dictionary.

# # Create a dictionary containing details of 3 students.

# # Each student should have Name, Age, Course and Marks.

# # Access and print the marks of one particular student.

# # Q22. Create a Dictionary Using zip().

# # Create two lists:

# # One containing 5 student names.

# # Another containing their marks.

# # Use zip() to create a dictionary where names are keys

# # and marks are values.

# # Print the dictionary.

# # Q23. Sort a Dictionary by Values.

# # Create a dictionary containing product names and prices.

# # Sort the dictionary by price in ascending order.

# # Store the sorted result in a NEW dictionary and print it.

# # Q24. Dictionary Comprehension.

# # Use dictionary comprehension to create a dictionary

# # containing numbers from 1 to 10 as keys and their squares

# # as values.

# # Print the dictionary.

# # Q25. Student Marks Management System.

# # Create a dictionary to manage student names and marks.

# # Implement the following operations:

# # 1. Add a new student.

# # 2. Update an existing student's marks.

# # 3. Search for a student's marks by name.

# # 4. Delete a student.

# # 5. Display all students and their marks.

# # 6. Find the student with the highest marks.

# #

# # Use loops, conditions and dictionary methods wherever needed.

# # Make the program menu-driven if you can.

# # ============================================================

# # EXTRA TOPICS TO PRACTISE AFTER Q25

# # ============================================================

# # 1. setdefault()

# # 2. fromkeys()

# # 3. copy() and shallow copying

# # 4. clear()

# # 5. del statement

# # 6. Dictionary comprehension

# # 7. Nested dictionaries

# # 8. zip()

# # 9. enumerate()

# # 10. sorted()

# # 11. Converting dictionaries to and from JSON
