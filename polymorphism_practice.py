# # ## Part 1: Method Overriding 

# # 1. Create an Animal parent class with a sound() method and override it in Dog and Cat child classes. class Animal:
class Animal:
    
    def sound(self):
        print("sounds")
        
class Dog(Animal):
    
    def sound(self):
        print("barking")
        
class Cat(Animal):
    
    def sound(self):
        print("mewoing")  
        
sound = Cat()
sound.sound()             
             
# # 2. Create an Employee parent class with a work() method and override it in a Manager child class.
class Employee:
    def work(self):
        print("Woking")
        
class Manager(Employee):
    def work(self):
        print("Manager is working")
        
obj1 = Manager()
obj1.work()                
# # 3. Create a Vehicle parent class with a start() method and override it in Car and Bike child classes.
class Vehical:
    def start(self):
        print("Starting...")
       
class Car(Vehical):
    def start(self):
        print("vehical is sarting..!")
        
car1 = Car()
car1.start()                    

# Part 2: Method Overloading 

## A. Using Default Arguments

# 1. Create a Calculator class with an add() method that accepts one, two, or three numbers.
class Calculator:
    
    def add(self,a = 0, b = 0 , c=0):
        print(a + b + c)
add = Calculator()
add.add(2,3,4)  
        
# 2. Create a Student class with calculate_marks() that accepts marks for one, two, or three subjects.

class Student:
    def calculate_marks(self,eng,math,hindi):
        print("Total marks:",eng + math + hindi)
cal = Student()
cal.calculate_marks(87,89,76)        

# 3. Create a Salary class with calculate_salary() that accepts basic salary, bonus, and optional incentives.
class Salary:
    def calculate_salary(self, salary , bonus,optional=0):
        self.salary = salary
        self.bonus = bonus
        self.optional = optional
        
        salary = bonus + optional + salary
        
        print("your salary is :",salary)
cal = Salary()
cal.calculate_salary(50000,5000,1000)        
        
# 4. Create an ElectricityBill class with calculate_bill() that accepts units and an optional fixed charge.
class ElectricityBill:
    def calculate_bill(self, units, fixed_charge=0):
        total = (units * 5) + fixed_charge
        print("Electricity Bill:", total)


bill = ElectricityBill()
bill.calculate_bill(100, 50)
bill.calculate_bill(100)

# 5. Create a Rectangle class with area() that accepts length and an optional breadth.
class Rectangle:
    def area(self, length, breadth=None):

        if breadth is None:
            print("Area of Square:", length * length)
        else:
            print("Area of Rectangle:", length * breadth)


r = Rectangle()
r.area(5)
r.area(5, 10)


# ### B. Using *args

# 6. Create a ShoppingCart class with calculate_total() that accepts any number of product prices.

class ShoppingCart:
    
    def calculated_total(self, * args):
        
        total = 0
        
        for i in args:
            total = total + i
        print(total)
            
p1 = ShoppingCart()
p1.calculated_total(10,20,30)
p1.calculated_total(50,30,30)
        
    
# 7. Create an Average class with calculate_average() that accepts any number of values.

class Average:
    def calculate_average(self,*args):
            
        count = 0
        total = 0
                            
        for i in args:

            total = total + i
            count = count + 1
            print("Avg" , total / count)
            
add = Average()
add.calculate_average(34,56,75,)            
              

# 8. Create a Company class with total_expenses() that accepts any number of expenses.

class Company:
    
    def total_expenses(self,*args):
        
        total = 0
        
        for i in args:
            total = total + i
            
        print(" total exp: ",total)
        
exp = Company()
exp.total_expenses(23,56)            
        
# 9. Create a Calculator class with multiply() that accepts any number of numbers.
class Calculator:
    
    def multiply(self, *args):
        
        result = 1
        for i in args:
            result = result * i
        print(result)
            
mul = Calculator()
mul.multiply(3,4)            

# 10. Create a Result class with total_marks() that accepts marks from any number of subjects.
class Result:
    def total_marks(self,*args):
        total = 0
        for  i in args:
            total = total + i
        print("total marks:",total)
s1 = Result()
s1.total_marks(70,80,90)        


# 11. **Restaurant Bill:** Create a Restaurant class with calculate_bill() that accepts food price, optional tax, and optional delivery charge using default arguments.
class Restraurant:
    def calculate_bill(self,food_price,tax,charges=0):
        print("food price:", food_price + tax + charges)
        
cust = Restraurant()   
cust.calculate_bill(50,5,5)     
        
# 12. **Employee Attendance:** Create an Attendance class with calculate_percentage() that accepts total working days and optional absent days using default arguments.
class Attendance:
    def calculate_percentage(self,*args, off_days = 5):
        mon = 30
        total = 0
        for i in args:
            total = total + i
            days = total - 5
        print("percentage of Total Working days : ", (days / mon )* 100)
emp1 = Attendance()
emp1.calculate_percentage(25)
       