cart = ["Shoes", "Watch", "Bag"]
# Add `"Mobile"` to the cart and display the updated cart.
cart.append("mobile")
print(cart)

subjects = ["Python", "SQL"]
new_subjects = ["Excel", "Power BI"]
# Add all new subjects to the existing list.
subjects.extend(new_subjects)
print(subjects)

patients = ["Amit", "Priya", "Rahul", "Sneha"]
# Insert `"Rohan"` at index 2.
patients.insert(2,"Rohan")
print(patients)


orders = ["Pizza", "Burger", "Pasta", "Dosa"]
# Remove `"Burger"` from the list and display the updated list.
orders.remove("Burger")
print(orders)


products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
# Remove the last product and display the removed product.
products.pop()
print(products)


cart = ["Shoes", "Watch", "Bag", "Mobile"]
# Remove all elements from the cart.
cart.clear()
print(cart)



marks = [75, 80, 65, 90, 85, 90]
# # Find the index of 90 and count how many times 90 appears.
print(marks.index(90))
print(marks.count(90))


salary = [25000, 40000, 18000, 50000, 30000]
# Sort the salaries in ascending order. Then sort them in descending order.
salary.sort()
print(salary)

salary.reverse()
print(salary)

products = ["Mobile", "Laptop", "Mobile", "Tablet", "Watch", "Laptop"]


# - Add a new product.
products.append("Power bank")
# - Insert a product at a specific position.
products.insert(3,"Home Theater")
# - Remove one product.
products.remove("Power bank")
# - Count the occurrences of `"Mobile"`\.\
print(products.count("Mobile"))   
# - Find the index of `"Tablet"`\.
print(products.index("Tablet"))
# - Create a separate copy of the final list.
print(products.copy())
print(products)


student = ("Vaishnavi", 22, "BCA", "Pune")
# Display the student's name, age, course, and city using indexing.
student.index(22)


employees = ("Amit", "Priya", "Rahul", "Sneha", "Karan")
# Display the first two employees and the last two employees using slicing.

for emp in employees:
    print(emp)


prices = (500, 1000, 500, 1500, 500, 2000)
# Count how many times 500 appears.
print(prices.count(500))

customers = ("Amit", "Priya", "Rahul", "Sneha", "Karan")
# Find the index position of `"Rahul"`\.
print(customers.index("Rahul"))

marks = (75, 85, 90, 65, 80)
# # Find the total, highest, lowest, and number of marks.

print("max :" ,max(marks))
print("min :" ,min(marks))
print(sum(marks))


# Create a tuple containing a student's name, roll number, and course. Unpack the tuple into three separate variables and display them.
info = ("Vaish" , 121 , "MCA")
first , second , third = info
print(first)
print(second) 
print(third)


numbers = (10, 20, 30, 40, 50)
# Convert the tuple into a list, modify its second element, and convert it back into a tuple.

list = list(numbers)
list.insert(1,70)
print(numbers)
print(list)

employees = (    ("Amit", 25000),    ("Priya", 30000),    ("Rahul", 35000))

student = {    "name": "Amit",    "age": 22,    "course": "BCA"}
# Add a city to the dictionary and update the student's age.
student.update({"city": "pune"})
print(student)

student.update({"age" : 25})
print(student)



employee = {    "id": 101,    "name": "Priya",    "salary": 30000,    "department": "IT"}

# Display all keys, all values, and all key-value pairs separately.
print(employee.keys())
print(employee.values())
print(employee.items())



products = {    "Laptop": 50000,    "Mobile": 20000,    "Tablet": 15000}
# Retrieve the price of `"Mobile"` and also try retrieving `"Watch"`\.
print(products.get("Mobile"))
print(products.get("Watch"))

customer = {    "id": 101,    "name": "Rahul",    "city": "Pune"}
# Remove `"city"` using `pop()` and display the removed value.
print(customer.pop("city"))



employee = {    "id": 101,    "name": "Sneha",    "salary": 35000}
# Remove the last inserted key-value pair and display the removed pair.
print(employee.popitem())


student = {    "name": "Amit",    "marks": 85,    "course": "Python"}
# Create a copy of this dictionary and modify the copied dictionary without changing the original.
new = student.copy()
new.update({"city" : "Pune"})
print(new)


employee = {    "name": "Rahul",    "salary": 40000}
# Add a `"department"` key with the default value `"IT"` only if it does not already exist.
employee.setdefault("department","IT") 
print(employee)

employee = {    "id": 101,    "name": "Amit",    "salary": 30000,    "department": "IT"}

# - Display all keys.
print(employee.keys)
# - Display all values.
print(employee.values())
# - Display all items.
print(employee.items())

# - Add a default value for `"city"` if missing.
print(staticmethod("city"))
# - Create a copy of the dictionary.
dict = employee.copy()
print(dict)

customers = {101, 102, 103, 104}

# Add customer ID 105 to the set.
customers.add(105)
print(customers)


students = {"Amit", "Priya", "Rahul"}

# Add multiple students: `"Sneha"`, `"Karan"`, and `"Neha"`\.
students.update(["sneha","Karan","neha"])
print(students)


products = {"Laptop", "Mobile", "Tablet", "Watch"}

# Remove `"Tablet"` from the set using `remove()`\.
products.remove("Tablet")
print(products)

products = {"Laptop", "Mobile", "Tablet", "Watch"}

# Try removing `"Camera"` using `discard()`\.
products.discard("camera")
print(products)


attendance = {"Amit", "Priya", "Rahul", "Sneha"}

# Remove all elements from the set.
attendance.clear()
print(attendance)

numbers = {10, 20, 30, 40, 50}


# Create a copy of this set and add 60 to the copied set.
backup = numbers.copy()
backup.add(60)
print(backup)

available_items = {"Pen", "Pencil", "Book", "Eraser"}

# Remove one arbitrary element and display the removed element.
available_items.pop()
print(available_items)

class_a = {"Amit", "Priya", "Rahul", "Sneha"}
class_b = {"Priya", "Sneha", "Karan", "Neha"}

print(class_a.intersection(class_b))


group_a = {101, 102, 103, 104}
group_b = {103, 104, 105, 106}

# - Find all customers from both groups.
print(group_a.union(group_b))
# - Find customers present only in group A.
print(group_a)
# - Find customers present only in group B.
print(group_b)

a = {10, 20, 30, 40}
b = {10, 20}
c = {50, 60}

# - Check whether `b` is a subset of `a`\.
print(b.issubset(a))
# - Check whether `a` is a superset of `b`\.
print(a.issubset(b))
# - Check whether `a` and `c` are disjoint.
print(a.isdisjoint(b))
# - Update `a` with all elements of `c`\.
print(a.update(c))
# - Find the intersection of `a` and `b`\.
print(a.intersection(b))
# - Update `a` by keeping only common elements with `b`\.

# - Update `a` by removing elements that are also present in `b`\.
print(a.difference_update(b))
# - Find the symmetric difference between `a` and `b`\.
print(a.symmetric_difference(b))
