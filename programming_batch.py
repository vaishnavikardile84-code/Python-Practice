num = int(input("Enter Number : "))

if num % 2 == 0 :
        print("Even")
else :
        print("Odd")
        
num = 12

if num > 0 :
    print("Positive")
elif num < 0:
        print("Negative")
        
else:
        print("Zero")
        
num = 1234
reverse = 0

for i in range (num):
    digit =  num % 10  
    reverse = reverse * 10 + digit 
    num = num // 10
    
print(reverse)  


num =1234
reverse = 0


i = 0
while num len(a):
    
    digit =  num % 10  
    reverse = reverse * 10 + digit 
    num = num // 10
    i+=1
    
print(reverse)      
   
   
num =1234
reverse = 0
original_num = 0


i = 0
while num > 0:
    
    digit =  num % 10  
    reverse = reverse * 10 + digit 
    num = num // 10
    i+=1
    
if original_num == reverse:
    print("palindrome")
else:
    print("Not palindrome")
     


num = 7

for i in range(2 , num):
        if num % 2 == 0:
                print("Not prime")
else:
                print("Prime") 
                
                
num = 7 

i = 2

while i < num:
    if num % i == 0:
        print("Not Prime")
    i=i+1    
else:
        print("Prime")
   
        
i = 1

while i < 100:
    
    if i % num == 0:
        print(i)  
    i=i+1
#q
num = 5

i = 1
fact = 1

while i <= num:
    fact = fact * i
    i += 1

print("Factorial:", fact)  

# find cube sq

num = 5

sq = num ** 2
cube = num ** 3

print("Square:", sq)
print("Cube:", cube)



name = "Vaish"

i = len(name) - 1

reverse = 0

while i >= 0:
    reverse = reverse + name[i]
    i = - 1

print("Reversed String:", reverse)





li = [12,34,2,23,43,34]

for i in li:
    if i % 2 == 0:
        print("Even", i)
    else :
        print("odd", i)

Ecount = 0
Ocount = 0

li = [12,34,2,23,43,34]

for i in li:
    if i % 2 == 0:
        Ecount = Ecount + 1    
        
    else :
        Ocount = Ocount + 1 
print("Count of Odd:", Ocount)
print("Count of even:", Ecount)

li = [12,34,2,23,43,34]

li = [12, 34, 2, 23, 43, 34]

reverse = []

for i in range(len(li)-1, -1, -1):
    reverse.append(li[i])

print("Reversed List:", reverse)




                    
li = [12, 34, 2, 23, 43, 34]

for num in li:

    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, "Not Prime")
                
        else:
            print(num, "Prime")

    else:
        print(num, "Not Prime")   

        
li = [12, 34, 2, "a", "vaish", 34]

for i in li:
    if type(i) == str:
        print(i)    
     
for i in li:
    if type(i) == int:
        print(i) 
        
student = {"name": "Vaishnavi","age": 22,"city": "Pune"}   

for i in enumerate(student):
    print(i)                 
    
stu = {'Vaishnavi': 85, 'Rani': 90, 'radha': 75, 'Shree': 95, 'nick': 80}

total = 0

for i in stu:
    total = total + i

print("Total Sum:", total)    


    
stu = {'Vaishnavi': 85, 'Rani': 90, 'radha': 75, 'Shree': 95, 'nick': 80}



for str, int in student.items():
    if int > 60:
        print(str, ":", int)  
    
student = {
    "Vaishnavi": 85,
    "Rani": 90,
    "Om": 45,
    "Shree": 95,
    "Rahul": 55
}

count = 0

for name in student:
    count += 1

print("Total Students:", count) 


student = {
    "Vaishnavi": 85,
    "Rani": 90,
    "Om": 45,
    "Shree": 95,
    "Rahul": 55
}

max_marks = 0

for name, marks in student.items():
    if marks > max_marks:
        max_marks = marks
        topper = name

print("Highest Marks:", max_marks)  



                
     
        
        
        
    
      
        

            
        
    
                
        
        