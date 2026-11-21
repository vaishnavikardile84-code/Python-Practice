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
        
features = Mobile("Iphone" , 2046,75000)
features.display()

# 4. Create a Rectangle class with length and width. Calculate area using a method.

class Reactange:
    
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def display(self):
        self.length* self.width
        print("area : " , self.length * self.width)
        
area = Reactange(3, 4)
area.display()            

# 5. Create a Circle class with radius. Calculate area using a method.
# 6. Create an Employee class with name, employee ID, and salary. Calculate annual salary.
# 7. Create a BankAccount class with account holder, account number, and balance. Implement
# deposit and withdrawal.
# 8. Create a Product class with product name, price, and quantity. Calculate the total bill.
# 9. Create a Student class with three subject marks. Calculate total, percentage, and result.
# 10. Create a Laptop class with brand, RAM, processor, and price. Display configuration.
# 11. Create a Book class with title, author, and price. Create a method to apply a 10% discount.
# 12. Create a Movie class with movie name, ticket price, and number of tickets. Calculate total ticket
# cost.
# Python OOP - Day 3 | Constructors Page 12 of 14
# 13. Create a ShoppingCart class with product price and quantity. Apply a 5% discount if the bill
# exceeds 5,000.
# 14. Create a Temperature class with Celsius value. Convert Celsius into Fahrenheit.
# 15. Create an ElectricityBill class with customer name and units consumed. Calculate the bill
# using unit rates you choose.
# 16. Create a Student class with default name as "Unknown" and age as 18 .
# 17. Create an Employee class with default department as "IT" and salary as 25000 .
# 18. Create a Mobile class with default brand as "Samsung" and price as 15000 .
# 19. Create a Car class with default colour as "White" and speed as 0 .
# # 20. Create a BankAccount class with a default balance of 1000 .

class BankAccount:
    def __init__(self, balance = 1000):
        self.balance= balance
        
    def display(self):
        print(self.balance)
ac1 = BankAccount(120)        
ac1 = BankAccount()        