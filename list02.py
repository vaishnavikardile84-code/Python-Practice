
## Q1. Positive and Negative Indexing

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[2]) #30
print(numbers[-1]) #60
print(numbers[-3])#40
print(numbers[1] + numbers[-2]) 

## Q2. List Slicing

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[1:5]) #(20,30,40,50)
print(numbers[:4]) #(10, 20, 30, 40)
print(numbers[3:]) #10, 20, 30
print(numbers[-4:-1]) #80 , 70, 60 ,50
print(numbers[::-1]) #80 , 70,6,05,50,40,30,20,10
print(numbers[6:2:-1]) #40, 50, 60, 


# Q3. Greater Than and Less Than


numbers = [12, 5, 18, 3, 25, 9]

for i in numbers:
    if i < 10:
        print(i) 
#12,18,25

# 1. What is the output?
# 2. What changes if `i > 10` becomes `i < 10`? - 5,3,9
# 3. What is the difference between `>` and `<`?

# Q4. Built-in Functions

marks = [45, 80, 65, 90, 35, 80]


print(len(marks))
print(max(marks)) 
print(min(marks))
print(sum(marks))
print(marks.sort())
print(marks.count(80))
print(marks.index(65))
# ```

# ### Q5. append(), extend(), and insert()

numbers = [10, 20, 30]

numbers.append([40, 50])
print(numbers)

numbers.extend([60, 70])
print(numbers)

numbers.insert(2, 25)
print(numbers)


# Explain the difference between `append()`, `extend()`, and `insert()`.

# Q6. copy() vs Assignment — MOST IMPORTANT


marks = [70, 80, 90]

y1 = marks.copy()
y2 = marks

y1.append(100)
y2.append(60)

print(marks is y1)

print("Original:", marks) 
print("Copy:", y1) #[70, 80, 90,100]
print("Assignment:", y2)  #[70, 80, 90,60]

# # Answer these questions:

# # 1. What is the output?
# # 2. Why does modifying `y1` not change `marks`?
# # 3. Why does modifying `y2` change `marks`?
# # 4. What is the difference between `y1 = marks.copy()` and `y1 = marks`?
# # 5. What happens when you write `marks = y1`?

# Q7. Replacing and Inserting Elements

numbers = [10, 20, 30, 40, 50]

numbers.insert(2, 99)
print(numbers)

numbers[3] = 77
print(numbers) #[10,20,99,77,30,40,50]


# Q8. Filtering Elements Using a for Loop

# Write a program that creates a new list containing only numbers greater than 20 and less than 60.

numbers = [12, 25, 60, 35, 18, 55, 20, 75, 45]
result = []
for i in numbers:
    if i > 20 and i < 60:
        result.append(i)
print(result)

# Q9. Counting Elements Using a while Loop

numbers = [10, 20, 30, 40, 50]
print(sum(numbers))

print(numbers.count(10))
avg = sum(numbers)/len(numbers)
print(avg)

# # Do not use `numbers = [10, 20, 30, 40, 50]

numbers = [10, 20, 30, 40, 50]

i = 0
total = 0
count = 0

while i < 5:
    total = total + numbers[i]
    count = count + 1
    
    i = i + 1
avg=total / count


print("Total:", total) 
print("Number of elements:", count) 
print("Average:", avg)      

# Q10. Masterji's Challenge — List Methods and Slicing

marks = [45, 78, 32, 90, 65, 28, 85, 50]

# 1. Print the total number of elements

i = 0
count = 0


while i < len(marks):
    count = count + 1
       
    i = i + 1
print(count)

# 2. Print the highest and lowest marks.

print(max(marks))
print(min(marks))

# 3. Print the first four elements using slicing.

marks = [45, 78, 32, 90, 65, 28, 85, 50]


print(marks[0 : 5])

# 4. Print the last three elements using negative slicing.


marks = [45, 78, 32, 90, 65, 28, 85, 50]


print(marks[-1: -4:-1 ])

# # 5. Create a copy of `marks` using `copy()`.

marks = [45, 78, 32, 90, 65, 28, 85, 50]


y1 = marks.copy()
y2 = marks

y1.append(100)
y2.append(20)

print(marks)
print(y1)
print(y2)


# # 5. Create a copy of `marks` using `copy()`.


marks = [70, 80, 90]

y1 = marks.copy()
y2 = marks

y1.append(100)
y2.append(60)

print(marks is y1)

print("Original:", marks) 
print("Copy:", y1) #[70, 80, 90,100]
print("Assignment:", y2)  #[70, 80, 90,60]



# # 6. Add `100` to the copied list without changing the original.
copied_marks = marks.copy()
copied_marks.append(100)
print(copied_marks)

# # # 7. Create a new list containing marks greater than or equal to 60 using a `for` loop.

marks = [45, 78, 32, 90, 65, 28, 85, 50]

copied = marks.copy()
filtered = [] 

for i in marks:
    
    if i >= 60 :
        

        filtered.append(i)

print(marks)
print(copied)
print(filtered)
