## Python Practice – Global, Nonlocal & Enclosing Scope

# **Q1. Reassignment**  
# Create a variable `price` with the value `500`. Reassign it to `750` and print the updated value.
price = 500
def reassign():
    price = 750
    print(price)
reassign()    

# **Q2. Local Variable**  
# Create a function `student_details()`. Inside it, create a local variable `student_name` and assign your name to it. Print the variable inside the function.
def student_details():
    stud_name = "Vaish"
    print(stud_name)
student_details()    

# **Q3. Global Variable – Reading**  
# Create a global variable `company = "TCS"`. Create a function `show_company()` that accesses and prints this variable.
# company = "TCS"
# def show_company(a):
#     pass
# show_company(company) 
   
company = "TCS"
def show_company():
    print(company)
show_company() 
      
# **Q4. Global Variable – Reassignment**  
# Create a global variable `account_balance = 10000`. Create a function `deposit()` that adds ₹2,000 to the existing balance using the `global` keyword.
account_balance = 10000
def deposite():
    global account_balance
    account_balance = account_balance + 2000
    print(account_balance)
deposite()
    
# **Q5. Global Variable – Multiple Updates**  
# Create a global variable `cart_total = 500`. Create two functions:
# - `add_item()` adds ₹300.
# - `apply_discount()` subtracts ₹100.

cart_total = 500

def add_item():
   global cart_total
   cart_total = cart_total + 300
   print(cart_total)
def apply_discount():
    global cart_total
    cart_total = cart_total - 100
    print(cart_total)
       
add_item()
apply_discount()
        
# Use both functions to update the global variable.

# **Q6. Enclosing Scope**  
# Create an outer function `employee_details()`. Inside it, create a variable `employee_name = "Rahul"`. 
# Create an inner function `display_details()` that accesses and prints `employee_name`.

def employee_details():
    emp_name = "Rahul"
    
    def display_details():
        print(emp_name)
        
    display_details()        
employee_details()        

# **Q7. Nonlocal – Reassignment**  
# Create an outer function `salary_details()`. Inside it, create `salary = 25000`. 
# Create an inner function `increase_salary()` that increases the salary by ₹5,000 using `nonlocal`.

def salary_details():
    salary = 25000
    
    def increase_salary():
        nonlocal salary
        salary = salary + 5000
        print(salary)
        
    increase_salary()  
salary_details()      

# **Q8. Nested Functions – Multiple Variables**  
# Create an outer function `order_details()` with two variables:
# - `product = "Laptop"`
# - `price = 50000`

def order_details():
    product = "Laptop"
    price = 50000
    
    def update_ordrs():
        nonlocal price
        price = price + 45000
        print(price)
        
    update_ordrs()     
order_details()

# Create an inner function `update_order()` that changes the price to ₹45,000 using `nonlocal`. Print the updated order details.

# **Q9. Global vs Nonlocal**  
# Create a global variable `count = 10`. Create an outer function with another variable `count = 20`.
# Inside the inner function, use `nonlocal` to increase the enclosing `count` by 5. Do not modify the global variable.
count = 10
def fun_outer():
    count = 20 
    def fun_inner():
        nonlocal count
        count = count + 5
        print(count)
        
    fun_inner()  
fun_outer()      

# **Q10. Real-Life Challenge**  
# Create a function `bank_account()` with a local variable `balance = 5000`.

# Inside it, create three nested functions:
# 1. `deposit()` – adds ₹2,000 to the balance.
# 2. `withdraw()` – subtracts ₹1,000 from the balance.
# 3. `check_balance()` – displays the current balance.

def bank_account():
    balance = 5000
    def deposit():
        nonlocal balance
        balance = balance + 2000
        def withdraw():
            nonlocal balance
            balance = balance - 1000
            def check_balance():
                print(balance)
                
            check_balance()        
        withdraw()
    deposit()
bank_account()    

# Use the appropriate keyword wherever required.
