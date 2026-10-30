# # Python Lists: 15 Questions to Master the Concepts

# ## Level 1: Build Your Foundation

# ### Question 1 — Positive and Negative Indexing

# Study this list:

# ```python
# numbers = [12, 25, 37, 48, 59, 63, 74]
# ```

# Without running the code, write the output of each statement:

# ```python
# print(numbers[0])
# print(numbers[3])
# print(numbers[-1])
# print(numbers[-3])
# print(numbers[2] + numbers[-2])
# ```

# **Your task:** Identify which element each index accesses before calculating the final result.

# ### Question 2 — Slicing Fundamentals

# Consider:

# ```python
# numbers = [10, 20, 30, 40, 50, 60, 70, 80]
# ```

# Find the output of each statement:

# ```python
# print(numbers[1:5])
# print(numbers[:4])
# print(numbers[3:])
# print(numbers[-5:-1])
# print(numbers[1:7:2])
# print(numbers[::-1])
# print(numbers[6:2:-1])
# ```

# **Important:** Pay close attention to the starting index, stopping index, and step. Remember that slicing excludes the stopping index.

# ### Question 3 — Understand `<` and `>` in a Loop

# Predict the output:

# ```python
# numbers = [12, 5, 18, 3, 25, 9]

# for i in numbers:
#     if i > 10:
#         print(i)
# ```

# Then answer these questions:

# 1. What will happen if `i > 10` is changed to `i < 10`?
# 2. What will happen if it is changed to `i >= 10`?
# 3. What will happen if it is changed to `i <= 10`?

# Explain the difference between the four conditions.

# ### Question 4 — Built-in Functions

# Consider:

# ```python
# numbers = [15, 8, 24, 8, 31, 14]
# ```

# Find the output of:

# ```python
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(sorted(numbers))
# print(numbers.count(8))
# print(numbers.index(24))
# ```

# Also answer:

# **What is the difference between `sorted(numbers)` and `numbers.sort()`?**

# ---

# ## Level 2: List Methods and Slicing

# ### Question 5 — `append()`, `extend()` and `insert()`

# Predict the final output:

# ```python
# numbers = [10, 20, 30]

# numbers.append([40, 50])
# numbers.extend([60, 70])
# numbers.insert(2, 25)

# print(numbers)
# print(len(numbers))
# ```

# Then explain:

# 1. How many elements did `append()` add to the outer list?
# 2. How many elements did `extend()` add?
# 3. At which index was `25` inserted?
# 4. Which existing elements shifted positions?

# ### Question 6 — Index Shifting and Replacement

# Consider:

# ```python
# numbers = [11, 22, 33, 44, 55]

# numbers.insert(2, 99)
# print(numbers)

# numbers[3] = 77
# print(numbers)
# ```

# Write both outputs.

# Then explain the difference between inserting an element at an index and replacing an element at an index.

# ### Question 7 — Slicing with Negative Indexes

# Consider:

# ```python
# numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45]
# ```

# Find the output:

# ```python
# print(numbers[-6:-2])
# print(numbers[-1:-6:-1])
# print(numbers[-2:-8:-2])
# print(numbers[-4:])
# print(numbers[:-3])
# ```

# **Your task:** For each slice, identify the starting position, stopping position, and step before writing the result.

# ### Question 8 — Modify a List Using Slicing

# Write a program that:

# 1. Creates a list containing the numbers from `10` to `100`, increasing by `10`.
# 2. Prints the first three elements using slicing.
# 3. Prints the last four elements using negative indexing and slicing.
# 4. Prints every second element.
# 5. Prints the list in reverse order using slicing.

# **Restriction:** Do not use a loop to generate the list. Focus on slicing.

# ### Question 9 — `copy()` Versus Assignment

# Predict the complete output:

# ```python
# marks = [70, 80, 90]

# y1 = marks.copy()
# y2 = marks

# y1.append(100)
# y2.append(60)

# print("Marks:", marks)
# print("Y1:", y1)
# print("Y2:", y2)
# ```

# Then explain:

# 1. Why does modifying `y1` behave differently from modifying `y2`?
# 2. Why does `marks` change after `y2.append(60)`?
# 3. What is the difference between `y1 = marks.copy()` and `y1 = marks`?

# ---

# ## Level 3: Logic-Building with Loops

# ### Question 10 — `for` Loop and List Filtering

# Write a Python program using a `for` loop to print all numbers **greater than 20 and less than 60** from this list:

# ```python
# numbers = [12, 25, 60, 35, 18, 55, 20, 75, 45]
# ```

# Requirements:

# * Use an `if` condition.
# * Use both `<` and `>` correctly.
# * Print only the numbers satisfying both conditions.
# * Do not use list methods to solve the filtering task.

# ### Question 11 — Sum and Average Using a `while` Loop

# Given:

# ```python
# numbers = [10, 20, 30, 40, 50]
# ```

# Write a program using a `while` loop to calculate and print:

# 1. The sum of all elements.
# 2. The number of elements.
# 3. The average of the elements.

# **Requirements:**

# * Do not use `sum()` or `len()` to calculate these results.
# * Use an index to access the list elements.
# * Make sure the loop terminates correctly.

# ### Question 12 — Count Positive, Negative, and Zero Values

# Given:

# ```python
# numbers = [12, -5, 0, 8, -2, 0, 15, -10, 4]
# ```

# Write a program using a `for` loop to count:

# 1. Positive numbers.
# 2. Negative numbers.
# 3. Zero values.

# Print all three counts separately.

# **Important:** A number equal to zero is neither positive nor negative.

# ### Question 13 — Create a New List Using a Loop

# Given:

# ```python
# numbers = [12, 7, 24, 9, 30, 11, 18, 5]
# ```

# Create a new list containing only the numbers divisible by both `2` and `3`.

# Requirements:

# * Use a `for` loop.
# * Use the modulo operator `%`.
# * Use an `if` condition.
# * Add qualifying elements to the new list using a list method.
# * Print the new list and its length.

# ### Question 14 — Reverse a List Using a `while` Loop

# Given:

# ```python
# numbers = [10, 20, 30, 40, 50, 60]
# ```

# Write a program that creates a **new list in reverse order** using a `while` loop.

# Requirements:

# * Do not use `reverse()`.
# * Do not use `reversed()`.
# * Do not use slicing.
# * Do not modify the original list.
# * Print both the original list and the new reversed list.

# This question will test your understanding of negative indexing, loop conditions, and index movement.

# ### Question 15 — Final Challenge: Multiple Concepts Together

# You are given a list of student marks:

# ```python
# marks = [45, 78, 32, 90, 65, 28, 85, 50, 78, 95]
# ```

# Write a Python program that completes all the following tasks:

# 1. Print the number of marks using a built-in function.
# 2. Print the highest and lowest marks.
# 3. Print the first four marks using slicing.
# 4. Print the last three marks using negative indexing and slicing.
# 5. Create a separate copy of `marks`.
# 6. Add `100` to the copied list without changing the original list.
# 7. Create another list containing marks greater than or equal to `60` using a `for` loop.
# 8. Count how many marks are less than `40`.
# 9. Calculate the total of all marks using a `while` loop without using `sum()`.
# 10. Print the original list, copied list, and filtered list separately.

# **Important:** Use the correct list methods, slicing, comparisons, and loops. Do not skip any task.

# ---

# ## Your Practice Plan

# | Session | Questions | Main focus                                         |
# | ------- | --------- | -------------------------------------------------- |
# | 1       | 1–4       | Indexing, slicing, comparisons, built-in functions |
# | 2       | 5–9       | List methods, index shifting, copying              |
# | 3       | 10–14     | Conditions, `for` loops, `while` loops, logic      |
# | 4       | 15        | Combined practical challenge                       |

# **My recommendation:** Start with Question 1 and work through them in order. Slicing is your weakest area, so give Questions 2, 7, and 8 extra attention.

# You don't have to finish all 15 in one sitting. The goal is to understand the logic well enough to explain your code to your teacher—not merely to get the output right.

# When you're ready, send me your **Question 1 answer first**. I'll check it before you move on.
