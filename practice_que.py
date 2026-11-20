
# Python Functions Practice – 8 Questions

# Q1. Create a function welcome_message() with no arguments and no return value. Print a welcome message.

def welcome_message():
    print("welcome")
welcome_message()

# Q2. Create a function calculate_bill(price, quantity) that accepts arguments, calculates the total bill, and prints it without using return.

def calculate_bills(price, quantity):
    print(price * quantity)
calculate_bills(27,2)    

# Q3. Create a function get_company_name() with no arguments that returns a company name. Call the function and print the returned value.

def get_company_name():
    return "mahindra"

result = get_company_name()
print(result)

# Q4. Create a function calculate_bonus
# (salary, bonus_percentage) 
# that accepts arguments, calculates the bonus, and returns the bonus amount. 
# Store and print the returned value.

def calculate_bonus(salary,bonus_percentage):
    bonus = salary * bonus_percentage / 100
    return bonus
answer = calculate_bonus(30, 3)
print(answer)
    
# Q5. Create a function calculate_total(*args) that accepts multiple 
# product prices, calculates their total, and returns the result.

def calculate_total(*args):
    total = 0
    for i in args:
        total = total + i 
    return total
result = calculate_total(100,260,300,450)
print(result)
    
# Q6. Create a function employee_profile(**kwargs) that accepts employee details (name, age, department, salary) and prints each detail using a loop.

def employee_profile(**kwargs):
    for key , value in kwargs.items():
        print(key,value)
        
employee_profile(name = "vaishn" , age = 43, Department = "IT", salary = 45000)
        
# Q7. Create a function order_summary(*args, **kwargs) that accepts multiple product names using *args and customer details using **kwargs. 
# Print both.

def order_summary(*args, **kwargs):
    print("products:")
    
    for i in args:       
            print(i)
            
    for j , k in kwargs.items():        
            print(j , k)
            
order_summary("laptop","earphone","mobile")
order_summary(name = "vaibhav",mob = 9836722374, email = "vaish@gmail.com")

# Q8. Create a function student_result(name, *marks, **details) that accepts a student name, multiple subject marks, and additional details. 
# Calculate total and average marks, print student information, and return total and average. Call the function and store both returned values separately.



def student_result( name , *marks,**details ):
    total = 0
    
    total = sum(marks)
    avg = total / len(marks)
    print(name)
    print(marks)
      
    
    for i in marks:
        print(i)
      
    for i,j in details.items():
        print( i,j)
        
    print("Total:", total)
    print("Average:", avg)    
    return total, avg
        
        
result = student_result("vaish", 98,88,90,97, roll_no = 123,gender = "female" , std = "MCA")

print(result)

def hello():
    print(500)
    return "hello"
    
    
result = hello()
print(result)    