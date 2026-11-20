# 1. Create a class Person. Store a person's name and age using a method. Display both details.

class Person:
    def show_details(self, name , age ):
        self.name = name 
        self.age = age
        
    def display(self):
        print("name:", self.name)
        print("age:", self.age)
            
obj = Person()

obj.show_details("Amit", 45)
obj.display()


# 2. Create a class Student. Store name, roll number, and course. Display the student details.

class Student:
    def stu_details(self,name,roll_num,course):
        self.name = name
        self.roll_num = roll_num
        self.course = course
    def display(self):
        print("name : " , self.name)
        print("roll_num :" , self.roll_num)

stud1 = Student()
stud1.stu_details("Vaish" , 123 , "MCA")
stud1.display()            
        
# 3. Create a class Calculator. Store two numbers and create separate methods for addition, subtraction, multiplication, and division.

class Calculator:
    def calculation(self, a,b):
        self.a = a
        self.b = b

    def display(self):
        print("Addition : " , self.a + self.b)
        print("Subtration : " , self.a - self.b)
        print("Divion : " , self.a * self.b)
        print("Multiplication : " , self.a / self.b)
                    
cal = Calculator() 
cal.calculation(250,450)
cal.display()

# 4. Create a class Square. Store the side length and calculate its area and perimeter.

class Square:
    def calculate(self, side , len ):
        self.side = side
        self.len = len
    def display(self):
        print("Area : " , (self.side * self.side) )
        print("Perimeter : " , (self.side * 4 ))

cal = Square()
cal.calculate(2,2)
cal.display()            

# 5. Create a class Rectangle. Store length and breadth and calculate its area and perimeter.

class Reactange():
    def calculate(self , len , bre , ):
        self.len = len
        self.bre = bre
    def display(self):
        print("Area : " , self.len * self.bre) 
        print("Premetr : " , (self.len * self.bre ) * 4)   
    
# 6. Create a class Employee. Store employee name and monthly salary. Display annual salary.

class Employee():
    def emp_details(self , name , salary , ):
        self.name = name 
        self.salary = salary
    def display(self):
        print("Annual Salary : " , self.salary * 12)

income= Employee()
income.emp_details("Vaishnavi" , 50000)
income.display()
                    
# 7. Create a class Number. Store one number and check whether it is positive, negative, or zero.

class Number:
    def check(self,num):
        self.num = num 
    def display(self):
        if self.num >= 1:
            print("Positive")
        elif self.num <0:
            print("Negative")
        elif self.num == 0:
            print("Zero")
                         
cal = Number() 
cal.check(4)
cal.display()       
        

# 8. Create a class EvenOdd. Store a number and check whether it is even or odd.

class EvenOdd:
    def calculation(self ,a ):
        self.a = a 
        
    def display(self):
        if self.a % 2 == 0:
            print("Even")
        else:
            print("Odd")
            
cal = EvenOdd()
cal.calculation(3) 
cal.display()           
        

# 9. Create a class Voting. Store a person's age and check whether the person is eligible to vote (18 or above).

class Voting:
    def peoples(self, age ):
        self.age = age
    def display(self):
        if self.age >= 18:
            print("You can vote")
        else:
            print("You can not vote") 
checking = Voting()
checking.peoples(45)
checking.display()               
        
# 10. Create a class Product. Store product name, price, and quantity. Calculate and display the total amount.

class Product:
    
    def product_list(self ,name, price, quanity ):
        self.price = price
        self.name = name
        self.quantity = quanity
        
    def display(self):
        print("Names ",self.name)
        print("Toatl : " ,self.price * self.quantity)
        
amount = Product()
amount.product_list("sugur", 40,4)
amount.display()

# 11. Create a class Mobile. Store brand, model, and price. Display the mobile details.

class Mobile:
    def mob1(self, brand , price,model):
        self.brand = brand
        self.price = price
        self.model = model
    def display(self):
        print("Brand :" , self.brand,"Price : " , self.price, "Model : " , self.model)   

details = Mobile()
details.mob1("Nokia", 4500, 1999)
details.display()         
        
# 12. Create a class BankAccount. Store account holder and balance. Add a deposit method that updates the
# balance.

class BankAccount():
    def acc1(self,ac_holder,balance):
        self.ac_holder = ac_holder
        self.balance = balance
            
    def add_money(self,deposite):
        self.deposite = deposite   
          
    def display(self):
        
        self.balance = self.deposite + self.balance
        
        print("Name : " , self.ac_holder)
        print("Balance : " , self.balance)  
        print("Deposited : " , self.deposite )      
         
transaction = BankAccount()
transaction.acc1("Vaibhavi Patil" , 75000) 
transaction.add_money(5000)
transaction.display()  
     
# # 13. Create a class Book. Store title, author, and price. Display all details.

class Book:
    
    def details(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
        
    def display(self):
        print(self.title)
        print(self.author)
        print(self.price)
                        
info = Book()
info.details("Overthing","niraz sox",2500)
info.display()
        
# # 14. Create a class Circle. Store radius and calculate area (3.14 × radius × radius).

class Circle:
    
    def fun(self,radius):
        self.radius = radius
        
    def display(self):
        print("area is " , 3.14 * self.radius * self.radius)    

cal=Circle()
cal.fun(4)
cal.display()
       
            
# # 15. Create a class Temperature. Store Celsius temperature and convert it into Fahrenheit.
class Temp:
    def calculation(self,celsius):
        self.celsius = celsius
        
    def display(self):    
        print("Fahrenheit : " , (self.celsius * 9/5) + 32)
        
cal = Temp()
cal.calculation(25)  
cal.display()      
        
    
# # 16. Create a class ExamResult. Store student name and marks. Display Pass if marks are 35 or more; otherwise
# # display Fail.
class ExamResult():
    
    def stud_name(self,name,marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        if self.marks >= 35 :
            print("pass")
        else:
            print("fails")
            
result = ExamResult()
result.stud_name("avani" , 36)
result.display()                  

# # 17. Create a class Car. Store brand, colour, and speed. Create a method to display details and another method to increase speed by a given amount.

class Car:
    def car1(self,brand,color,speed):
        self.brand = brand
        self.color = color
        self.speed = speed
    def display(self):
        print("Brand : " , self.brand)
        print("color : " , self.color)
        print("speed : " , self.speed)
    def increase_speed(self):
        print("increased speed : " , self.speed + 250)
      
model = Car()
model.car1("mahindra","black",300)
model.display()
model.increase_speed()        
                     
# # 18. Create a class Movie. Store movie name, language, and rating. Display the movie information.

class Movie:
    
    def info(self,name,lang,rating):
        self.name = name
        self.lang = lang
        self.rating = rating
        
    def display(self):
      print("name : " , self.name)
      print("language : " ,  self.lang)
      print("rating : " , self.rating)
      
review = Movie()
review.info("ONE","English" , 4 )
review.display()        
            
        
# 19. Create a class ATM. Store account balance. Create methods for deposit and withdrawal, and display the updated balance. Do not allow withdrawal above the available balance.

class ATM:
    
    def account(self,balance):
        self.balance = balance
        
    def deposite(self,deposited_bal):
        self.deposited_bal = deposited_bal
        
    def withdraw(self,withdraw_money):
        self.withdraw_money = withdraw_money
        
           
    def display(self):
        
        print("Updated balance : " , (self.deposited_bal+self.balance) - self.withdraw_money)    
        
        if self.withdraw_money > self.deposited_bal+self.balance:
            
                print("You can not withdraw")
        else:
                print("You can")    
        
transaction = ATM()
transaction.account(25000)    
transaction.deposite(5000) 
transaction.withdraw(45)   
transaction.display() 
    

# # 20. Create a class Team. Create three different objects representing three players. Store each player's name and jersey number, then display all three players' details.

class Team:
    def plye1(self,name1 , jersey_num1):
        self.name1 = name1 
        self.jersey_num1 = jersey_num1

    def plyr2(self,name2 , jersey_num2):
        self.name2 = name2 
        self.jersey_num2 = jersey_num2    
        
    def plye3(self,name3 , jersey_num3):
        self.name3 = name3 
        self.jersey_num3 = jersey_num3   
            
    def display(self):
        print("pleayer 1 : " , self.name1, "jersey_no : " , self.jersey_num1)
        print("pleayer 2 : " , self.name2, "jersey_no : " , self.jersey_num2)
        print("pleayer 3 : " , self.name3, "jersey_no : " , self.jersey_num3)  
           
info = Team()
info.plye1("virat",237)
info.plyr2("Rohit",987)
info.plye3("Surya",234)
info.display()
        