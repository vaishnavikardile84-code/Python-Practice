# 1. Create a Hospital parent class with hospital_name and location. Create a Doctor child class with
# doctor_name and specialization.
class Hospital:
    def __init__(self,hospital_name , location):
        self.hospital_name = hospital_name
        self.location = location
       
    def display(self):
        print("Name of hospital :" , self.hospital_name)
        print("Location of hospital : " , self.location)    
        
class Doctor:
    def __init__(self,doc_name,specialization):
        self.doc_name = doc_name  
        self.specializaton = specialization
        
    def display(self):
        print("Name of doc :" , self.doc_name)
        print("spe of doc : " , self.specializaton)      

hosp1 = Hospital("Shraddha Clinics","Kada")
doc1 = Doctor("Dr.Khilare","Dermatologyst")
hosp1.display() 
doc1.display() 

# 2. Create Product with product_id and product_name. Create ElectronicProduct with warranty_years.
      
        
class Product:
    def __init__(self,product_name,product_id):
        self.product_name = product_name
        self.product_id = product_id
        
    def display(self):
        print("Product name : " , self.product_name)
        print("Product id :", self.product_id) 
        
class EletronicsProduct(Product):
    
    def __init__(self, product_name, product_id, warranty_years):
        super().__init__(product_name, product_id)
        self.warranty = warranty_years
        
    def display(self):
        print("Warranty yrs :" , self.warranty)
        print("Product name : " , self.product_name)
        print("Product id :", self.product_id)         

p1 = Product("laptop",2134)
E_p1 = EletronicsProduct("Mobile",2134,1)

p1.display()
E_p1.display()            

# 3. Create two parent classes MusicPlayer and Camera. 
# Create a SmartDevice child that inherits both.
class MusicPlayer:
    
    def __init__(self):
        print("Playing music")
        
class Camera:
    
    def __init__(self):
        print("Clicking")
        
class SmartDevice( MusicPlayer ,Camera ):
    
    def __init__(self):
        MusicPlayer.__init__(self)
        Camera.__init__(self)
    
device = SmartDevice()
# 4. Create Animal → Mammal → Dog using multilevel inheritance.

class Animal:
    def display(self):
        print("class Animal")
        
class Mammal(Animal):
    def __init__(self):
        print("Class Mammal")
        
class Dog(Mammal):
    def __init__(self):
        print("Class Dog")
        super().display()
        
pet = Dog()
pet.display()
                       
# 5. Create School as a parent and Teacher, Student and
# OfficeStaff as child classes.

class School:
    
    def display(self):
        print("School")
        
class Teacher(School):
    def t_display(self):
        print("Teacher") 
                   
class Student(School):
    def display(self):
        print("Student")
        
class Office_staff(School):
    def display(self):
        print("Office_staff")
        super().display()
        
obj1 = Office_staff()
obj1.display()  

obj2 = Teacher()
obj1.display()       
                
# 6. Create Person, Athlete and Student. Create StudentAthlete inheriting Athlete and Student.

class Person:
    
    def display(self):
        print("parent class")
        
class Athelete():
    
    def display(self):
        print("playing ", self.play)    
   
class Student(Athelete):
    
    def display(self):
        print("studying", self.play)    
    
class Studen_Athelet(Student, Athelete ):
      
    def display(self):
        print("studying and playing ")        
        
obj = Studen_Athelet()
obj.display()
            
# 7. Create a parent class with a parameterized initializer and pass values from the child using super().

class Parent:
    
    def __init__(self, name ):
        self.name = name
        
    def display(self):    
        print("Name :" , self.name)
        
class Child(Parent):
    def __init__(self):
        super().__init__("vaish")
                
obj1 = Child()
obj1.display()

# 8. Create a parent method calculate_salary(). Override it in PermanentEmployee and ContractEmployee.
class Parent:
    
    def calculate_salary(self):
        pass


class PermanentEmployee(Parent):

    def calculate_salary(self):
        print("Permanent Employee Salary")


class ContractEmployee(Parent):

    def calculate_salary(self):
        print("Contract Employee Salary")


p1 = PermanentEmployee()
p2 = ContractEmployee()

p1.calculate_salary()
p2.calculate_salary()  
 
# 9. Create two parent classes with a method named info(). Inspect the child class MRO and explain which method executes.

class Father:
    def info(self):
        print("Father info")


class Mother:
    def info(self):
        print("Mother info")


class Child(Father, Mother):
    pass


obj = Child()

obj.info()

print(Child.mro())
        

# 10. Create Library with library_name. Create Book with title and author. Decide whether inheritance or composition is the better design and justify your choice.
class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book(self):
        print("Title:", self.title)
        print("Author:", self.author)


class Library:

    def __init__(self, library_name, book):
        self.library_name = library_name
        self.book = book

    def display_library(self):
        print("Library:", self.library_name)
        self.book.display_book()


b1 = Book("Python Programming", "John")
l1 = Library("Central Library", b1)

l1.display_library()