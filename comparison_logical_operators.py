# Mixed Practice — Comparison + Logical Operators

# **Q1. Age & Driving License — Beginner**
# A person is 20 years old.
# Check whether the person is eligible for a driving license.
# **Condition:** age must be **18 or older**.

age = int(input("Enter age : "))

print(age >= 18 )

# ---

# **Q2. Shopping — Beginner**
# You have ₹5,000. A laptop bag costs ₹2,500.
# Check whether you can afford it.

# Use `>=`.
budget = 5000
bag = 2500

print("Yes, you can buy",budget >= bag)

# ---

# **Q3. Exam Result — Beginner**
# A student scored:

Python = 75
SQL = 68

# The student passes only if:

# * Python marks are **60 or more**
# * **AND** SQL marks are **60 or more**

print(Python >= 60 and SQL >= 60)


# **Q4. Movie Entry — Beginner/Medium**
# A movie is allowed only for people who are **18 or older**.
# A person is 17.

# Check whether the person can enter.

age = 17 
print(age >= 18)

# **Q5. Employee Bonus — Medium**
# An employee gets a bonus if:

# * Salary is **₹30,000 or more**
# * **AND** performance score is **80 or more**

# Given:

# ```python
# salary = 35000
# performance = 85

salary = 35000
score = 80

print(salary >= 30000 and score >= 80)


# **Q6. Scholarship — Medium**
# A student gets a scholarship if:

# * Marks are **90 or more**
# * **OR** attendance is **95 or more**

# Given:

# ```python
# marks = 88
# attendance = 97
marks = 88
attendance = 97

print(marks >= 90 or attendance >= 95 )

# **Q7. Online Shopping — Medium**
# A customer gets free delivery if:

# * Order amount is **₹1,000 or more**
# * **AND** the customer is a premium member.

# Given:

# ```python
# order_amount = 1200
# premium_member = True

order_amount = 1200
premium_memb = True

print(order_amount >= 1000  and premium_memb == True)


# **Q8. Job Eligibility — Medium/Tricky**
# A company accepts a candidate if:

# * Age is **between 21 and 30**
# * **AND** Python score is **70 or more**
# * **AND** SQL score is **60 or more**

# Given:

# ```python
age = 24
python_score = 75
sql_score = 62

print(age > 21 and age < 30 and python_score >= 70 and sql_score >= 60 )

# **Q9. Bank Loan — Tricky**
# A person can get a loan if **either**:

# * Monthly salary is ₹50,000 or more
#   **OR**
# * Credit score is 750 or more.

# Given:

# ```python
# salary = 42000
# credit_score = 780
# ```

# Check whether the person is eligible.

salary  = 42000
credit_score = 750 

print(salary >= 50000 and credit_score >= 750)

# **Q10. Internship Selection — Advanced 🔥**
# A company selects a student if:

# * Age is **18 or older**
# * **AND**
# * Python score is **70 or more**
# * **AND**
# * SQL score is **60 or more**
# * **AND**
# * Either:

#   * Power BI score is **70 or more**
#   * **OR** Excel score is **80 or more**
# ```python
age = 21
python_score = 76
sql_score = 65
powerbi_score = 68
excel_score = 85


print(
    age >= 18
    and python_score >= 70
    and sql_score >= 60
    and (powerbi_score >= 70 or excel_score >= 80)
)