# PYTHON – ENCAPSULATION PRACTICE

# Q1. Student Class

class StudentQ1:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks


s1 = StudentQ1("Vaishnavi", 98)

print("Name:", s1.name)
print("Marks:", s1.get_marks())


# Q2. Employee Class

class EmployeeQ2:

    def __init__(self, name, department, salary):
        self.name = name
        self._department = department
        self.__salary = salary

    def display(self):
        print("Name:", self.name)
        print("Department:", self._department)
        print("Salary:", self.__salary)


e1 = EmployeeQ2("Ayana", "Finance", 45000)
e1.display()


# Q3. Private Variable

class BankAccountQ3:

    def __init__(self, balance=5000):
        self.__balance = balance

    def display(self):
        return self.__balance


ac1 = BankAccountQ3()

try:
    print(ac1.__balance)
except AttributeError:
    print("Private variable cannot be accessed directly!")

print("Balance:", ac1.display())


# Q4. Getter Method

class StudentQ4:

    def __init__(self, marks=85):
        self.__marks = marks

    def get_marks(self):
        return self.__marks


s2 = StudentQ4()
print("Marks:", s2.get_marks())


# Q5. Setter Method

class Mobile:

    def __init__(self, price=15000):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


mob1 = Mobile()

print("Old Price:", mob1.get_price())

mob1.set_price(18000)

print("Updated Price:", mob1.get_price())


# Q6. Getter and Setter

class Product:

    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


product1 = Product(1200)

print("Old Price:", product1.get_price())

product1.set_price(150)

print("Updated Price:", product1.get_price())


# Q7. Bank Account

class BankAccountQ7:

    def __init__(self, balance=10000):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Enter a valid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid withdrawal amount!")
        elif self.__balance >= amount:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance!")

    def check_balance(self):
        print("Balance:", self.__balance)


ac2 = BankAccountQ7()

ac2.deposit(5000)
ac2.withdraw(5000)
ac2.check_balance()


# Q8. Employee Salary

class EmployeeQ8:

    def __init__(self, salary, name):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
            print("Salary updated successfully!")
        else:
            print("Salary must be greater than zero!")


e2 = EmployeeQ8(50000, "Vaishnavi")

print("Employee:", e2.get_name())
print("Original Salary:", e2.get_salary())

e2.set_salary(60000)

print("Updated Salary:", e2.get_salary())


# Q9. ATM PIN Verification

class ATM:

    def __init__(self, pin=1234):
        self.__pin = pin

    def verify_pin(self, pin):
        if self.__pin == pin:
            print("Correct PIN!")
        else:
            print("Incorrect PIN!")


atm1 = ATM()

atm1.verify_pin(1234)
atm1.verify_pin(123)