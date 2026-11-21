# 1. Create a Student class with a parameterized initializer for name, roll number, and age. Display
# the details.

class Student:
    def __init__(self,name,roll_number ,age ):
        self.name = name
        self.roll_number = roll_number
        self.age = age
        
    def details(self):
        print("Name :" , self.name)
        print("Roll no : " , self.roll_number)
        print("age : " , self.age)
        
stud1 = Student("Vaish",21,22)
stud1.details()
        
# 2. Create a Mobile class with brand, model, and price. Display mobile details.
class Mobile:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model 
        self.price=price
        
    def display(self):
        print("Brand : ", self.brand)
        print("Model : ", self.model)
        print("Price : ", self.price)
features = Mobile("Iphone" , 2046,75000)
features.display()
   
# 3. Create a Car class with brand, colour, and speed. Create three objects with different values.

class Car:
    def __init__(self,brand,speed,color):
        self.brand = brand
        self.speed = speed 
        self.color = color
                
    def display(self):
        print("Brand : ", self.brand)
        print("Speed : ", self.speed)
        print("Color : ", self.color)
        
features = Car("Iphone" , 2046,75000)
features.display()

# 4. Create a Rectangle class with length and width. Calculate area using a method.

class Reactange:
    
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def display(self):
        print("area : " , self.length * self.width)
        
area = Reactange(3, 4)
area.display()            

# 5. Create a Circle class with radius. Calculate area using a method.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculation(self):
        print("Area:", 3.14 * self.radius * self.radius)


circle1 = Circle(5)
circle1.calculation() 
        
# 6. Create an Employee class with name, employee ID, and salary. Calculate annual salary.
class Employee:
    
    def __init__(self, name , emp_id , salary):
        self.name = name 
        self.emp_id = emp_id
        self.salary = salary
        
    def display(self):
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Annual Salary:", self.salary * 12)
    
info = Employee("Vish", 123 , 45000) 
info.display()
            
# 7. Create a BankAccount class with account holder, account number, and balance. Implement deposit and withdrawal.

class BankAccount:
    def __init__(self, ac_holder, ac_number, balance):
        self.ac_holder = ac_holder
        self.ac_number = ac_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful:", amount)
        else:
            print("Insufficient balance!")

    def display(self):
        print("Account Holder:", self.ac_holder)
        print("Account Number:", self.ac_number)
        print("Balance:", self.balance)


ac1 = BankAccount("Vaish", 1234, 45000)
ac1.deposit(5000)
ac1.withdraw(10000)
ac1.display()       
            
# 8. Create a Product class with product name, price, and quantity. Calculate the total bill.
class Product:
    
    def __init__(self,name , price , quantity):
        self.name = name 
        self.price = price
        self.quantity = quantity
        
    def display(self):
        print("Product:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total Bill:", self.price * self.quantity)


product1 = Product("Laptop", 50000, 2)
product1.display()
# 9. Create a Student class with three subject marks. Calculate total, percentage, and result.
class Student:
    def __init__(self, marathi, hindi, english):
        self.marathi = marathi
        self.hindi = hindi
        self.english = english

    def display(self):
        total = self.marathi + self.hindi + self.english
        percentage = (total / 300) * 100

        print("Total:", total)
        print("Percentage:", percentage)

        if self.marathi >= 35 and self.hindi >= 35 and self.english >= 35:
            print("Result: Pass")
        else:
            print("Result: Fail")


sub = Student(87, 94, 78)
sub.display()

# 10. Create a Laptop class with brand, RAM, processor, and price. Display configuration.
class Laptop:
    
    def __init__(self,brand , RAM, processor,price):
        self.brand = brand 
        self.ram = RAM 
        self.processor = processor
        self.price = price
        
    def disply(self):
        print("Brand : " , self.brand)    
        print("ram  : " , self.ram)    
        print("Processor : " , self.processor)    
        print("Price : " , self.price)   
        
check_configuration = Laptop("DELL" , "RAM","RYZEN" , 90000)
check_configuration.disply()         
        
# 11. Create a Book class with title, author, and price. Create a method to apply a 10% discount.
class Book:
    def __init__(self,title , author , price ):
        self.title = title 
        self.author = author
        self.price = price
    def discout(self):
        discount_amount = self.price * 0.10
        final_price = self.price - discount_amount

        print("Title:", self.title)
        print("Author:", self.author)
        print("Original Price:", self.price)
        print("Discount:", discount_amount)
        print("Final Price:", final_price)
            
            
info = Book("OVERTHINKING" , "Vaish" , 150)
info.discout            
# 12. Create a Movie class with movie name, ticket price, and number of tickets. Calculate total ticket cost.
class Movie:
    
    def __init__(self,movie_name , ticket_price , no_of_ticket):
        self.movie_name = movie_name
        self.no_of_ticket = no_of_ticket
        self.ticket_price = ticket_price
        
    def calc(self):
        total_cost = self.no_of_ticket * self.ticket_price
        print("Total cost : " , total_cost)
            
ticket = Movie("Ramayan" , 350 , 4) 
ticket.calc()  
         
# 17. Create an Employee class with default department as "IT" and salary as 25000 .

class Employee:
    def __init__(self,department="IT",salary = 2500):
        self.department = department
        self.salary = salary
        
    def display(self):
        print(self.department,self.salary) 
                
info = Employee("finance")  
info.display()      
        
        
# 18. Create a Mobile class with default brand as "Samsung" and price as 15000 .
class Mobile:
    
    def __init__(self,brand = "samsung" , price = 1500):
        self.brand = brand
        self.price = price
        
    def display(self):
        print(self.brand,self.price)   
         
features = Mobile() 
features.display()      

# # 20. Create a BankAccount class with a default balance of 1000 .

class BankAccount:
    
    def __init__(self, balance = 1000):
        self.balance= balance
        
    def display(self):
        print(self.balance)
        
ac1 = BankAccount(120)   
ac1.display()
     
ac2 = BankAccount()        
ac2.display()