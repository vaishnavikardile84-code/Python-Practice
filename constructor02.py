# 1. Create a Student class with set_details(name, rollno, course) and show() methods, create three objects, and display their details.
class Student:
        
    def set_details(self):
        
        self.name = "Vaish"
        self.roll_num = 123
        self.course = "MCA"
        
    def show(self):
        print("name :" , self.name)
        print("roll num :" , self.roll_num)
        print("Course : " , self.course)
        
s1 = Student()
s1.set_details()
s1.show() 
           
# 2. Create an Employee class with set(name, salary) and calc() methods to calculate and display the annual salary.
class Employee:
    
    def __init__(self):
        self.salary = 45000
        self.name = "vaish"
        
    def calc(self):
        self.annual = self.salary * 12
        # return self.annual
    
    def disply(self):
        print("Annual salary : " , self.annual)
        
E1=Employee()
E1.calc()
E1.disply()        
            
# 3. Create a Mobile class with brand, model, and price using a default constructor, and create display_details() and apply_discount(discount) methods.
class Mobile:
    def __init__(self,brand = "sSquare",model = 2026, price = 45000):
        self.brand = brand
        self.model = model
        self.price = price
    def display(self):
        discount_amount = self.price * 0.5
        final_price = discount_amount - self.price
        print("final price : ",final_price)
mob1=Mobile()
mob1.display()    
            
        
# 4. Create a BankAccount class with account holder name and balance, and implement deposit(amount), withdraw(amount), and display_balance() methods with an insufficient balance check.
class BankAccount:
    def __init__(self):
        self.account_holder = "Vaish" 
        self.balance = 45000
        self.w_amount = 500
        self.d_amount = 300
        
    def deposite(self,):
        self.balance += self.d_amount
        print("deposited amt " , self.d_amount)
    
    def withdrawal(self):  
       
        if self.balance >=  self.w_amount:
            self.balance-= self.w_amount
            print("Withdrawal sucessful " , self.w_amount)
        else:
            print("Insufficient Balance")
   
    def display(self):
        print("Account holder name : " , self.account_holder)   

        print("balance : ",self.balance)
        
ac1 = BankAccount()
ac1.deposite()
ac1.withdrawal()
ac1.display()          
        
# 5. Create a Car class with car name, rent per day, and rental days, and calculate and display the total rent.
class Car:
    def __init__(self,):
        self.rent = 200
        self.days = 3
    def display(self):
        total_rent = self.rent * self.days
        print("Total rent : " , total_rent)
car1 = Car()
car1.display()
          
# 6. Create a Book class with a parameterized constructor accepting book name, author name, and book price, and create two objects with different information.
class Book:
    def __init__(self,book,author,price):
        self.book = book
        self.author = author
        self.price = price
    def display(self): 
        print("Book :" , self.book)   
        print("Price :" , self.price)   
b1 = Book("AntiCode","Kivet",450)
b1.display()

b2 = Book("Semicolon_Safaristory", "Grevy jems",550)
b2.display()
    
# 7. Create a Rectangle class with a parameterized constructor accepting length and width, and create a calculate_area() method.
class Reactange:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def calculate(self):
        area = self.length * self.width
        print("Area of square : " , area)
cal = Reactange(3,5)
cal.calculate()
            
# 8. Create an ElectricityBill class with customer name and units consumed, and calculate the bill using ₹5 for the first 100 units, ₹7 for the next 100 units, and ₹10 for units above 200.
class Elecericity_Bill:
    
    def __init__(self,name , units):
        self.name = name 
        self.units = units
        
    def calculate(self):
        
        print("Name :" , self.name)
        print("Units : ", self.units)
        
        if self.units == 100 :
            print(5," Rupees")
        elif self.units == 200: 
            print(7," Rupees")
        elif self.units >= 200:
            print(10," Rupees")

bill1 = Elecericity_Bill("Atharv",500)    
bill1.calculate()
      
# 9. Create a Product class with product name, price, and quantity, and implement display_product(), calculate_total_price(), and update_quantity(new_quantity) methods.
class Product:
    def __init__(self,name , price , quantity ):
        self.name = name
        self.price = price
        self.quantity = quantity
    def display_product(self):
        self.price*=self.quantity
        
        print("Name : " ,self.name)
        print("Price : " ,self.price)   
product1 = Product("Nayra" , 5 , 3)
product1.display_product()

product2 = Product("Myra" , 3 , 9)
product2.display_product()         
    
# 10. Create an Employee class with company_name and employee_count as class variables and employee_name and 
# employee_id as instance variables, and increase the employee count whenever an object is created.

class Employee:
    
    company_name = "mahindra"
    emp_count = 230
    
    def __init__(self,emp_name , emp_id):
        self.emp_name = emp_name
        self.emp_id = emp_id
        Employee.emp_count += 1
        
    def display(self):
        print("Company Name :" , self.company_name)
        print("Employee Name : " , self.emp_name)
        print("Empployee Id : " , self.emp_id)
        print("Total Emp Count : " , self.emp_count)
        print("-------------------------------------")
        
emp1=Employee("kaustubh" , 231)
emp1.display()

emp2 = Employee("Tani",232)
emp2.display()        
        
# 11. Create a Student class with school_name as a class variable, student_name and roll_number as instance variables, and percentage as a local variable inside a method.
class Student:
    school_name = "Amolak School"
    
    def __init__(self,student_name , roll_number ):
        
        self.school_name = student_name
        self.roll_number = roll_number
        
    def display(self):
        percentage = 0
        print("Percentage :" , percentage )
        print("School name : " , self.school_name )
        print("Roll Number : " , self.roll_number )
stud1 = Student("Ketan", 34)
stud1.display()        
            
        
# 12. Create a Patient class with hospital_name as a class variable and paclastient_name, patient_age, and disease as instance variables, then create three patient objects and display their details.
class Patient:
    hospital_name = "sSquare Hospital"
    
    def __init__(self,paclastient_name, patient_age,disease):
        self.paclastient_name= paclastient_name
        self.patient_age = patient_age
        self.disease=disease
    def display(self):
        print("paclastient name : " , self.paclastient_name)
        print("patient age : " , self.patient_age)
        print("Disease : " , self.disease)
        
p1 = Patient("xyz",34,"dengue")
p1.display()        
            
# 13. Create a Course class with institute_name as a class variable, course_name and course_fee as instance variables, and a discount variable inside a method to calculate the final course fee.
class Course:
    institude_name = "The Kiran Academy"
    def __init__(self, data_analytics , course_fees):
        self.data_analytics = data_analytics
        self.course_fees = course_fees
    def display(self):
        
        final_course_fees = self.course_fees
        print("Institude Name : " , self.institude_name)
        print("Course name = ", self.course_fees)
        print("Course Fess " , final_course_fees)    
        
# 14. Create an ATM class with account holder name and balance, and implement check_balance(), withdraw(amount), and deposit(amount) methods, where withdraw() returns the updated balance.
class ATM:
    def __init__(self,ac_holder , balance):
        self.ac_holder = ac_holder
        self.balance = balance
    def check_balance(self):
        print("Total balance : " , self.balance )        

    def deposit(self,amount) :
        self.balance += amount        
            
    def withdraw(self,w_amount):
        self.w_amount = w_amount
        
        if self.balance >=  self.w_amount:
            self.balance-= self.w_amount
            print("Withdrawal sucessful " , self.w_amount)
        else:
            print("Insufficient Balance")    

ac1 = ATM("Vaishnavi",25000)
ac1.check_balance()
ac1.deposit(40)
ac1.withdraw(20)
           
# 15. Create a Temperature class with Celsius temperature and implement celsius_to_fahrenheit() and fahrenheit_to_celsius(fahrenheit) methods that return converted temperatures.

class Temperature:
    
    def __init__(self, celsius):
        self.celsius = celsius

    def celsius_to_fahrenheit(self):
        fahrenheit = (self.celsius * 9/5) + 32
        return fahrenheit

    def fahrenheit_to_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius

temp = Temperature(37)
print("Celsius to Fahrenheit:", temp.celsius_to_fahrenheit())
print("Fahrenheit to Celsius:", temp.fahrenheit_to_celsius(98.6))   
temp2 = Temperature(40)    
print("fahrenheit_to_celsius", temp2.fahrenheit_to_celsius(98.0))
        
#16 Create a Vehicle class with vehicle_count as a class variable and vehicle_name, vehicle_type, and vehicle_price as instance variables,
# and implement display_details(), calculate_insurance(rate), and update_price(new_price) methods.
class Vehicle:
    
    vehicle_count = 0

    def __init__(self, vehicle_name, vehicle_type, vehicle_price):
        self.vehicle_name = vehicle_name
        self.vehicle_type = vehicle_type
        self.vehicle_price = vehicle_price

        Vehicle.vehicle_count += 1

    def display_details(self):
        print("Name:", self.vehicle_name)
        print("Type:", self.vehicle_type)
        print("Price:", self.vehicle_price)

    def calculate_insurance(self, rate):
        insurance = self.vehicle_price * rate / 100
        return insurance

    def update_price(self, new_price):
        self.vehicle_price = new_price
        return self.vehicle_price


vehicle1 = Vehicle("Verna", "Car", 1000000)

vehicle1.display_details()

insurance = vehicle1.calculate_insurance(1.5)
print("Insurance Amount:", insurance)

vehicle1.update_price(1100000)
print("Updated Vehicle Price:", vehicle1.vehicle_price)

print("Total Vehicles:", Vehicle.vehicle_count)   

