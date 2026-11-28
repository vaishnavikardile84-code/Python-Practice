
# 1. Student Management System
# Create a Student class with:
# - Instance variables: name, roll_no, marks.
# - Create a constructor to initialize student details.
# - Create a method display_details() to display student information.
# - Create three student objects and display their details.
class Student:
    
    def __init__(self,name,roll_no , marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        
    def display(self):
        print("Name : " , self.name)
        print("Roll number : " , self.roll_no)
        print("marks :" ,self.marks)
        
stud1 = Student("Vaishnavi",121,98)
stud1.display()
print("------------------------------")        

stud2 = Student("Rani",122,99) 
stud2.display()           
print("------------------------------")        
stud3 = Student("Punam", 123, 97) 
stud3.display()           

# 2. Bank Account – Encapsulation
# Create a BankAccount class with:
# - Private variable __balance.
# - Constructor to initialize account holder name and balance.
# - Create deposit() method to add money.
# - Create withdraw() method to withdraw money.
# - Create display_balance() method.
# - Do not allow withdrawal if the amount exceeds the available balance.
class BankAccount:
    
    def __init__(self, balance, holder_name):
        self.__balance = balance
        self.holder_name = holder_name

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.__balance and amount > 0:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance or invalid amount")

    def display_balance(self):
        print("Account Holder:", self.holder_name)
        print("Available Balance:", self.__balance)


account1 = BankAccount(10000, "Vaish")

account1.deposit(50)
account1.withdraw(500)
account1.display_balance()

# 3. Employee Salary – Inheritance
# Create a parent class Employee with:
# - Variables: name, employee_id, salary.
# - Method display_employee().
# Create a child class Manager with:
# - Additional variable department.
# - Method display_manager().
# Use inheritance to access the parent class properties and methods.

class Employee:
    
    def __init__(self,name,employe_id,salary):
        self.name = name
        self.employee_id  = employe_id
        self.salary = salary
        
    def display_employee(self):
        print("name",self.name)
        print("employee_id",self.employee_id)
        print("Employee salary", self.salary)
    
class manager(Employee):  
    def __init__(self,name,employee_id,salary,department):
        super().__init__(name,employee_id,salary)
        self.department = department   
     
    def display_manager(self):
        print("department" ,self.department)       
    
obj1 = manager("Vaish",121,5000,"IT")
obj1.display_manager()
obj1.display_employee()


# 4. Payment System – Polymorphism
# Create three classes:
# - CreditCard
# - UPI
# - NetBanking
# Each class should have a method called payment().

# Implement the method differently in each class to display the respective payment method.

# Call the same method using different objects.
class Creditcard:
    def payment(self):
        print("cash")
    
class UPI:
    def payment(self):
        print("phone pay")
    
class NetBanking:
    def payment(self):
        print("upi")    
           
obj1 = Creditcard()
obj2 = UPI()
obj3 = NetBanking()

obj1.payment()
obj2.payment()
obj3.payment()    