# # PYTHON – ENCAPSULATION PRACTICE

# # Q1. Student Class
# Create a Student class with:
# - Public variable: name
# - Private variable: __marks
# - Create an object and display both values.
class Student:
    def __init__(self, name, mark):
        self.__name = name
        self.__mark = mark
        
    def get_marks(self):    
        return self.__mark
    
s1 = Student("Vaishnavi",98)
print(s1.get_marks())


# print(s1.__name)
# print(s1.get_marks())

  
# # Q2. Employee Class
# Create an Employee class with:
# - Public variable: name
# - Protected variable: _department
# - Private variable: __salary
# - Display all three variables using an object.

class Employee:
    def __init__(self,name, department, salary):
        self.name = name
        self._department = department
        self.__salary = salary
        
    def display(self):
        return self.name    
        
s1=Employee("Ayana","Finance",45000)
print(s1.name)
# print(s1._department)
# print(s1.__salary)       
        
        
# # Q3. Private Variable
# Create a BankAccount class.
# - Declare a private variable __balance = 5000.
# - Create an object.
# - Try accessing __balance directly outside the class.
# - Observe the output or error.

class BankAccount:
    
    def __init__(self,balance = 5000):
        self.__balance = balance 
        
    def display(self):
        return self.__balance
    
ac1 = BankAccount()
# print(ac1.__balance)        
    
# # Q4. Getter Method
# Create a Student class.
# - Declare a private variable __marks = 85.
# - Create a getter method get_marks().
# - Access marks using the getter method.
class Student:
    
    def __init__(self,marks = 85 ):
        self.__marks = marks
    def get_marks(self):
        return self.__marks
    
s1 = Student()
print(s1.get_marks())      
        
# # Q5. Setter Method
# Create a Mobile class.
# - Declare a private variable __price = 15000.
# - Create a setter method set_price().
# - Update the mobile price to 18000.
# - Display the updated price.

class Mobile:
    
    def __init__(self,price = 15000):
        self.__price = price
        
    def get_price(self):
        return self.__price
    
    def set_price(self,price):
        self.__price = price
    
mob1 = Mobile()

print(mob1.get_price())  

mob1.set_price(18000)

print("updated price : " , mob1.get_price())     
        
        
# # Q6. Getter and Setter
# Create a Product class.
# - Declare a private variable __price.
# - Create a getter method to access the price.
# - Create a setter method to update the price.
# - Create an object and update the price.
class Product:
    
    def __init__(self,price):
        self.__price = price
        
    def get_price(self):
        return self.__price
    
    def set_value(self,price):
        self.__price = price
    
product1 = Product(1200)

print("Old Price : ", product1.get_price()) 

product1.set_value(150)

print("Updated price " , product1.get_price())  
        

# # Q7. Bank Account
# Create a BankAccount class with:
# - Private variable __balance = 10000.
# - Method deposit(amount) to deposit money.
# - Method withdraw(amount) to withdraw money.
# - Method check_balance() to display the balance.
# - Do not allow withdrawal if the amount exceeds the balance.

class BankAccount:
    
    def __init__(self,balance = 10000):
        self.__balance = balance
        
    def deposite(self,amount):
        self.__balance += amount
        print("deposited:",amount)
    
    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print("withdraw:",amount)
        else:
            print("Insufficient Balance ! ")
            
    def check_balance(self):
        print("Balance : " , self.__balance)
             
            
ac1 = BankAccount()

ac1.deposite(5000)
ac1.withdraw(5000)
ac1.check_balance()
        
# # Q8. Employee Salary
# Create an Employee class with:
# - Private variables __name and __salary.
# - Create a getter method for salary.
# - Create a setter method for salary.
# - Allow salary updates only if the new salary is greater than zero.

class Employee_salary:
    
    
    def __init__(self,salary,name):
        self.__name = name
        self.__salary = salary
        
    def get_info(self):
        return self.__salary   
    def set_info(self):
        return self.__name
    
e1 = Employee(50000,"Vaishnavi")
print("Original value", e1.get_info())
print("Updated",e1.set_info())
         
# # Q9. ATM PIN Verification
# Create an ATM class with:
# - Private variable __pin = 1234.
# - Create a method verify_pin(pin).
# - Check whether the entered PIN

class ATM:
    def __init__(self,pin = 1234):
        self.__pin = pin
        
    def verify_pin(self,pin):
        if self.__pin == pin:
            print("Correct pin ")
        else:
            print("Incorrect pin")
enter = ATM()
enter.verify_pin(123)            