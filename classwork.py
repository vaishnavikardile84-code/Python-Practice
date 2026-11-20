class ShoppingCart:
    
    def set_details(self,customer_name , product_name,quantity):
        self.customer_name = customer_name
        self.product_name = product_name
        self.quantity = quantity
        
    def calculate_total(self,price):
        self.price = price
        self.total = self.price * self.quantity
        
    def apply_discount(self,discount):
        self.discount = discount
        
        if self.total > 5000:
            self.discount = self.total * 10 / 100         
        
    def display_bill(self):
        print("name :" , self.customer_name)
        print("product : " , self.product_name) 
        print("discount applied :" , self.discount )  
        print("total : " , self.total ) 
        print("final amount : " , self.total- self.discount)    
        
transc = ShoppingCart()
transc.set_details("Vanita","mobile",1)
transc.calculate_total(15000)  
transc.apply_discount(1000)  
transc.display_bill()    


class Library_Book:
    def set_details(self,book_name , author_name,is_available ):
        self.book_name = book_name
        self.author_name = author_name
        self.is_available = is_available
        
    def is_issue_book(self):
        if self.is_available == True:
            self.is_available = False
            
    def return_book(self):
        self.is_available = True
        
    def display_details(self):
        print("Name :" ,self.book_name)
        print("Author Name : " , self.author_name)
        print("Availability : ", self.is_available)
        
info = Library_Book()
info.set_details("Oxford","Nick johns",True)
info.is_issue_book()
info.return_book()
info.display_details()            
            
class ElectricityBill:
    def set_details(self):
        self.customer_name = "Atharv"
        self.units_consumed = 700

    def calculate_bills(self):
        if self.units_consumed <= 100:
            self.total_bill = self.units_consumed * 3

        elif self.units_consumed <= 200:
            self.total_bill = (100 * 3) + ((self.units_consumed - 100) * 5)

        else:
            self.total_bill = (100 * 3) + (100 * 5) + ((self.units_consumed - 200) * 8)

    def display_bill(self):
        print("Name:", self.customer_name)
        print("Total Units:", self.units_consumed)
        print("Total Bill:", self.total_bill)


amt = ElectricityBill()
amt.set_details()
amt.calculate_bills()
amt.display_bill()        
            
             
               
            
            
        