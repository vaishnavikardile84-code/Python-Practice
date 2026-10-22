# # # Grade = "A"

# # # match Grade :
# # #     case  "A" :
# # #         print("A Grade  range --90 to 100" )
# # #     case  "B" :
# # #         print("B grade range -- 80 to 70 ")
# # #     case  "C" :
# # #         print("C grade range -- 60 to 50") 
# # #     case  "D" :
# # #         print("D grade range -- 40 to 35") 
# # #     case "E" :
# # #         print("Failed  range -- less than 35") 
# # #     case _ :
# # #         print("Enter valid Grade")      
        
# # # Quarter = int(input("Enter Months : "))

# # # match Quarter :
# # #     case 1|2|3 :
# # #         print("Quarter 1 ") 
        
# # #     case 4|5|6 : 
# # #         print("Quarter 2")                  
    
# # #     case 7|8|9 :
# # #         print("Quarter 3") 
# # #     case 10 |11|12 :
# # #         print("Quarter 4")       
# # #     case _:
# # #         print("Enter valid querter number ")  
        

# # # A = int(input("Enter number A "))
# # # B = int(input("Enter number B "))
# # # Operator = input("Enter an arithematic operator ")

# # # match Operator :
# # #     case "+" :
# # #         print("Case 1 executed ! Addition of A + B is : " , A + B)
# # #     case "-" :
# # #         print("Case 2 executed ! Substraction of A - B is : " ,A - B) 
# # #     case "*" :
# # #         print("Case 3 executed ! Multiplication of A * B : " , A * B)
# # #     case "/" :
# # #         print("Case 4 executed ! Multiplication of A / B :" , A / B )
# # #     case "%" : 
# # #         print(" Case 5 executed ! Moduls of A / B is :", A % B)
# # #     case "//" :
# # #         print(" Case 6 executed ! Floor division of A + B is " ,  A // B)
# # #     case _ :
# # #         print(" Case 7 executed ! Please Enter Valid Operator ")  
        
        
        
# # # # vowels = "a " , "e " , "i" , "o " , "u"
        
# # # Vowels = input("Please Enter Vowels : ")
 
# # # match Vowels :
# # #     case "a" :
# # #             print("You enterd a vowels : ")  
# # #     case "e" :
# # #             print("You enterd e vowels : ")  
# # #     case "i" :
# # #             print("You enterd i vowels : ")  
# # #     case "o" :
# # #             print("You enterd o vowels : ")  
# # #     case "u" :
# # #             print("You enterd u vowels : ")                        
# # #     case _ :
# # #             print("You enterd consonant")                   
    
        
# # number = int(input("Enter a number :"))

# # match number :
# #     case 1 :
# #         print("One")
# #     case 2 :
# #         print("Two")
# #     case 3 :
# #         print("Three") 
# #     case 4:
# #         print("Four")
# #     case 5 :
# #         print("Five")
# #     case _:
# #         print("Please enter valid number")                     

# # Plan_Code = int(input("Enter a number :"))

# # match number :
# #     case 1 :
# #         print("Your plan includes 1 GB per day")
# #     case 2 :
# #         print("Your plan includes 2 GB per day")
# #     case 3 :
# #         print("Your plan includes 3 GB per day") 
# #     case 4:
# #         print("Your plan includes 4 GB per day")
# #     case 5 :
# #         print("Your plan includes 4 GB per day")
# #     case _:
# #         print("Please enter valid number")           


# # Plan_Code = int(input("Enter setting choice :"))

# # match number :
# #     case 1 :
# #         print("Wi-Fi")
# #     case 2 :
# #         print("Bluetooth")
# #     case 3 :
# #         print("Airplane Mode") 
# #     case 4:
# #         print("Mobile Data")
# #     case 5 :
# #         print("Battery Saver")
# #     case _:
# #         print("Please enter valid setting choice")   
        
               
# # Extension = input("Enter file extension : ")
# # match Extension:
# #     case ".py":
# #         print("Python File")
# #     case "sql":
# #         print("SQL File")
# #     case "csv":
# #         print("CSV Data File")
# #     case "xlsx":
# #         print("Excel File")
# #     case ".pdf":
# #             print("PDF File")    
# #     case _ :
# #         print("Please Enter Valid File Name")     
        
        
# # Category = input("Enter Your Category : ")
# # match Category :
# #     case "Child" :
# #         print("Child - 0% Concession")
# #     case "Student" :
# #         print("Student - 10% Concession")
# #     case "Senior":
# #         print("Senior - 20 % Concession")
# #     case "General":
# #         print("General - 0% Concession")
# #     case _:
# #         print("Enter valid category")
                                               
# Commands = input("Enter SQL Commands : ")
# match Commands :
#     case "DDL":
#         print("Defines Database structure")
#     case "DML" :
#         print("Modify Data")
#     case "DQL":
#         print("Retrive data")
#     case "TCL":
#         print("Manage transaction")
#     case _ :
#             print("Enter valid command")      
    
# # Write a program that accepts an employee's role and displays the permitted system a    
        
# Role = input("Enter your roll in company :")
# exprience = int(input("Enter Your Exprience :"))

# match Role:
#     case "Admin":
#         print("Full Access ")
        
#         if exprience >= 2 :
#             print("Exprienced ")
#         else :
#             print("Fresher")  
              
#     case "Analyst":
#         print("Report and Dashboard")                                                                      
#     case "Developer":
#         print("Development tools")
#     case "Intern":
#         print("Read - Only Access") 
    
#     case "boss":
#         print("You are boss ")
#         if exprience == 1 :
#             print("Exprienced")
#         else :
#             print("Not Exprienced")
#     case _ :
#             print("Enter valid roll")                 
                      
# #  Write a program that accepts a tool name and displays its primary purpose.        
# Tools = input("Enter tool name" )

# match Tools :
#     case "Excel":
#         print("Excel Spreadsheet calculations and analysis ")
#     case "sql" :
#         print("sql Database querying")  
#     case "powerBi" :
#         print("power bi Interactive Dash board")
#     case "tableau" :
#         print("tableau Data visualization")
#     case _ :
#         print("Tool Not Found ")              

# Write a program that accepts a payment method and calculates the 
# final amount after applying a method-specific discount.
(chat gpt pested)

amount = int(input("Enter purchase amount: "))
payment_method = input("Enter your payment method: ").strip().lower()

match payment_method:
    case "upi":
        discount = 15
    case "credit card":
        discount = 3
    case "debit_card":
        discount = 2
    case "cash":
        discount = 0
    case _:
        print("Enter a valid payment method")
        discount = -1

        if discount != -1:
            discount_amount = amount * discount / 100
            final_amount = amount - discount_amount


        print("Discount percentage:", discount, "%")
        print("Discount amount:", discount_amount)
        print("Final amount to pay:", final_amount)
