# 1. Create a Student class with a private name and private marks. Add methods to display the details and update marks. Marks must be between 0 and 100.
class Student:
    
    def __init__(self,name,marks):
        self.__name = name
        self.__marks = marks
        
    def display_details(self):
        print("Name : " , self.__name)
        print("Marks : " , self.__marks)    
        
    def update_marks(self,marks):
        
        if 0 <= marks <= 100:
            self.__marks = marks 
            print("Updated marks")
        else:
            print("Invalid marks")
            
        print("Marks : " , self.__marks)
  
stud = Student("vaish",98)
stud.update_marks(85)
stud.display_details()
        
# 2. Create a BankAccount class with a private balance. Add deposit(), withdraw() and check_balance() methods. Reject zero or negative transaction amounts.
class BankAccount:
    
    def __init__(self,balance):
        self.__balance = balance
        
    def deposite(self,amount):
        if amount > 0:
            self.__balance += amount  
            print("Amount Deposited")
        else:
            print("Invalid amount")
              
    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid amount")
        elif self.__balance >= amount:
            self.__balance-= amount  
            print("Withdraw Sucessful")
        else:
            print("Insufficient Balance")
            
    def check_balance(self):
        print("Balance : " , self.__balance)              

account = BankAccount(5000) 

account.deposite(500)
account.withdraw(1000)
account.check_balance()    
    
# 3. Create an Employee class with private employee_id and salary. Add getter methods and a setter that accepts only a positive salary.

class Employee:
    
    def __init__(self,emp_id,salary):
        self.__emp_id = emp_id
        self.__salary = salary
        
    def get_salary(self):
        print("Emp Id:" ,self.__emp_id)
        print("Salary : " , self.__salary)
        
    def set_salary(self, amount):
        if amount >= 0:
            self.__salary = amount
            print("salary updated")
        else:
            print("invalid salary")  

emp1 = Employee(123,45000) 
emp1.set_salary(35000)
emp1.get_salary()             
                  
# 4. Create a Mobile class with a private password. Add methods to verify the password and change it only when the old password is correct.
class Mobile:
    def __init__(self,password):
        self.__password = password
        
    def verify(self,password):
        if self.__password == password:
            print("Correct password")
        else:
            print("Wrong passsword")
           
pass1 = Mobile(123)  
pass1.verify(123456)

# 5. Create a Car class with private speed. Add accelerate() and brake() methods. Speed must never become
# negative and must not exceed 180.

class Car:
    
    def __init__(self,speed):
        self.speed = speed
    
    def acceleration(self,speed):
        speed >= 0 and speed < 180
        if self.speed > speed:
            self.speed += speed
        print("speed of car : ", self.speed)    
            
    def car_break(self):
        if self.speed > 0:
           breaking = 0   
           print("breaking car...!")
           
car1 = Car(40)
car1.acceleration(50)
car1.car_break()           
                 
# 6. Create a Product class with private name and price. Use @property to read the price and a setter to reject a price less than or equal to zero.
class Product:
    def __init__(self,name,price):
        self.__name = name
        self.__price = price
        
    @property
    def read_price(self):
        return self.__price
    
    @read_price.setter
    def read_price(self,value):
       if value > 0:
           self.__price = value
       else:
           print("Invalid price")
           
           
product1 = Product("vaish",250)
print(product1.read_price)
product1.read_price = 500
print(product1.read_price)
product1.read_price = -100
       
# 7. Create a LibraryBook class with a private availability status. Add issue_book() and return_book() methods. A book cannot be issued twice without being returned.
class Library_Book:
    def __init__(self,available):
        self.__available = available
        
    def issued_book(self):
        if self.__available > 0:
            self.__available -= 1
            print("Book is issued ")
        else:
            print("book is not available")
            
    def return_book(self):
        self.__available += 1
        print("Returnd book")
        
    def check_available(self): 
        print("Available book : " , self.__available)           
    
book1 = Library_Book(2)
book1.issued_book()
book1.return_book()
book1.check_available()  
    
# 8. Create a Wallet class with private balance. Add add_money() and spend_money() methods. Spending must not exceed the available balance.
class Wallet:
    
    def __init__(self, balance):
        self.__balance = balance
        
    def add_money(self,amount):
        self.__balance += amount
        print("Added money:", self.__balance)
        
    def spend(self,amount):
        self.__balance > amount           
        self.__balance -= amount
        print("Spended money:", self.__balance)
   
expences = Wallet(500)  
expences.add_money(50)
expences.spend(25)      
            
# 9. Create an ElectricityBill class with private units. 
# Add a setter that rejects
# negative units and a method to
# calculate the bill using your own slab rates.

class ElectricityBill:
    
    def __init__(self,unit):
        self.__unit = unit
        
    def get_unit(self):
        print(self.__unit)
    
    def set_unit(self):
        if  self.__unit < 0 :
            print("Invalid units")
        
    def calculate(self):
        if self.__unit >= 0 and self.__unit <= 100:
            print("3 Rupees",self.__unit * 3)
        elif self.__unit >= 101 and self.__unit <= 200:
            print("5 Rupees",self.__unit * 5)
        elif self.__unit >= 201 and self.__unit <= 300:
            print("7 rupees",self.__unit * 7)
        elif self.__unit > 300 :
            print("10 Rupees",self.__unit * 7)
bill = ElectricityBill(250)

bill.set_unit()
bill.calculate()
bill.get_unit()        
            
# 10. Create a ShoppingCart class with a private total and private item count. Add methods to add an item, 
# remove an item and display the cart summary. Do not allow the total or item count to become negative.
class ShoppingCart:
    
    def __init__(self):
        self.__total = 0
        self.__count = 0

    def add_items(self, price, quantity):
        if price > 0 and quantity > 0:
            self.__total += price * quantity
            self.__count += quantity
            print("Items added successfully")
        else:
            print("Invalid price or quantity")

    def remove_items(self, price, quantity):
        if price <= 0 or quantity <= 0:
            print("Invalid price or quantity")

        elif quantity > self.__count:
            print("Not enough items in cart")

        elif price * quantity > self.__total:
            print("Invalid removal amount")

        else:
            self.__total -= price * quantity
            self.__count -= quantity
            print("Items removed successfully")

    def display_cart(self):
        print("Total Items:", self.__count)
        print("Total Amount:", self.__total)


cart = ShoppingCart()

cart.add_items(100, 2)
cart.add_items(200, 1)

cart.display_cart()

cart.remove_items(100, 1)

cart.display_cart()  
        
        
            
                
        
