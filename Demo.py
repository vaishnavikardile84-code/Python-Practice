#Customer:** Customer_ID, First_Name, Last_Name, Email, Phone, Date_of_Birth, City, Registration_Date, Membership_Type, Is_Active

#Employee:** Employee_ID, First_Name, Last_Name, Email, Phone, Job_Title, Department, Salary, Joining_Date, Manager_ID

#Vehicle:** Vehicle_ID, Customer_ID, Vehicle_Number, Brand, Model, Vehicle_Type, Fuel_Type, Manufacturing_Year, Purchase_Date, Insurance_Expiry_Date


#Customer

customer_id = 121
first_name = 'Ram'
Last_name = 'patil'
Email = 'ram123@gmail.com'
Phone = 9233829117
Date_Of_Birth = 19
City = 'Pune'
Reg_Date = 20
Memb_Type = 'Premiume'
Is_Active = 'Active'






print("Customer_id is : " , customer_id , "First Name is :" , first_name , "Last_name is :", Last_name , "Email :", Email, "Phone" ,Phone , "Date_Of_Birth" , Date_Of_Birth,"City" ,City , "Reg_Date" , Reg_Date , "Memb_Type" , Memb_Type, "Is_Active" ,Is_Active)

#Employee:** Employee_ID, First_Name, Last_Name, Email, Phone, Job_Title, Department, Salary, Joining_Date, Manager_ID

Employee_ID = 111
First_Name = 'Vaish'
Last_Name = 'Kardile'
Email = 'vaish@gmail.com'
Phone = 9811238716
Job_Title = 'Data Analyst'
Salary = 45000
Joining_Date = 12 
Manager_ID = 123

print("Employee_id : " , 111)
print("First_Name : " , First_Name)
print("Last_Name : ", Last_Name)
print("Email :" , Email)
print("Phone :" , Phone)
print("Job_Title : ", Job_Title)
print("Salary :", Salary , "Joining_Date : " ,Joining_Date , "Manager_ID : ", Manager_ID)

#Vehicle:** Vehicle_ID, Customer_ID, Vehicle_Number, Brand, Model, Vehicle_Type, Fuel_Type, Manufacturing_Year, Purchase_Date, Insurance_Expiry_Date


#Vehical
Vehical_ID = 121
Customer_ID = 111
Vehical_Number = 1234
Brand = 'Mahindra'
Model = '12cabc'
Vehical_Type = 'Jeep'
Fuel_Type = 'Petrol'
Manufacturing_Year = 2023
Purchase_Date = 2026
Insurance_Expiry_Date = 2027

print("Vehical id : " , Vehical_ID, "\nCustomer_id " , Customer_ID , "\nBrand", Brand , "\nModel : "  , Model , "\nVehical_Type" ,  Vehical_Type , "\nFuel_Type" , Fuel_Type , "\nManufaturing year : ",Manufacturing_Year , "\nPurchase_Date ", Purchase_Date , "\nInsurance_Expiry_Date ", Insurance_Expiry_Date)
 
print(type(Fuel_Type))