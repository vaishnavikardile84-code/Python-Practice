#1) factorial
#A) No Args and without return

def factorial():
    fact = 1
    for i in range(1,4):
        fact = fact * i
    print(fact)
    
factorial()        

#B) No Args and with return
def factorial():
    fact = 1
    for i in range(1,5):
        fact = fact * i
    return fact

result = factorial()
print(result)                

#C) With args and without return

def factorial(a):
    
    fact = 1
    for i in range(1 , a + 1):
        fact = fact * i
        
    print(fact)
    
factorial(5)        

#D) With args and with return

def factorial(a):
    fact = 1
    for i in range(1 , a + 1):
        fact = fact * i
    return fact

result = factorial(12)
print(result)

#2) Fib

#2.A) No Args and without return

def fibnacci():
    n = 5
    a = 0
    b = 1
    for i in range(n+1):
        print(a)
        c = a + b
        a = b
        b = c
fibnacci()    
    
#2.B) No Args and with return

def fibnacci():
    n = 6
    a = 0 
    b = 1
    series = []
    for i in range(n + 1):
        series.append(a)
        c = a + b
        a = b
        b = c
    return series

result = fibnacci()    
print(result)

#2.c) With args and with return    

def fibnacci(n):
   
    a = 0 
    b = 1
    series = []
    
    for i in range(n + 1):
        series.append(a)
        c = a + b
        a = b
        b = c
    return series
    
result = fibnacci(7)        
print(result)         

#2.D) With args and with return

def fibnacci(n):
    
    a = 0 
    b = 1
    series = []
    for i in range(n + 1):
        series.append(a)
        c = a + b
        a = b
        b = c
    return series
    
result = fibnacci(7)  
print(result)

# #3) Armstrong
# #3.A) No args without return 

def armstrong():
    num = 153
    original = num
    total = 0
    length = len(str(num))

    for i in range(length):
        digit = num % 10 
        total = total + digit ** length
        num = num // 10
    if total == original:
        print("Armstrong number ")
    else : 
        print("Not armstrong number ")

armstrong()        

#2.B) No args with return

def armstrong():
    
    num = 123
    original = num
    total = 0  
    length = len(str(num))   
    
    for i in range(length):
        digit = num % 10
        total = total + digit  ** length
        num = num // 10
        if total == original:
            return "Armstrong"
    else:
        return "Not Armstrong"
        
result = armstrong()   
print(result)   

#3.C) args without return  

def armstrong(num):
    
    original = num
    total = 0
    length = len(str(num))

    for i in range(length):
        digit = num % 10 
        total = total + digit ** length
        num = num // 10
    if total == original:
        print("Armstrong number ")
    else : 
        print("Not armstrong number ")

armstrong(153)     

#3. D) args with return  

def armstrong(num):
    
   
    original = num
    total = 0  
    length = len(str(num))   
    
    for i in range(length):
        digit = num % 10
        total = total + digit ** length
        num = num // 10
        if total == original:
            return "Armstrong"
        else:
           return "Not Armstrong"
        
result = armstrong(150)   
print(result)

#4.A) No args with return

def prime():
    num = 6

    if num <= 1:
        return "Not a Prime Number"

    for i in range(2, num):
        if num % i == 0:
            return "Not a Prime Number"

    return "Prime Number"


answer = prime()
print(answer)

#4.B) No args without return

def prime():
    num = 9
    if num <= 1:
        print("Not a Prime Number")

    for i in range(2, num):
        if num % i == 0:
            print("Prime Number")
    
prime()

#4.C)args without return

def prime(num):

    if num <= 1:
        print("Not a Prime Number")

    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime Number")
        else:
            print("not prime num")
prime(6)

#4.D)args with return

def prime(num): 
    if num <= 1:
        return "Not a Prime Number"

    for i in range(2, num):
        if num % i == 0:
            return "Not a Prime Number"
    return "Prime Number"
answer = prime(9)
print(answer)

#5.A) No args with return

def even_odd():
    num = 5
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
result = even_odd()
print(result)  
    
#5.B) No args without return   

def even_odd():
    num = 8
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd()

#5.C) args without return   

def even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd(8)

#5.C) args with return   
def even_odd(num):
    

    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = even_odd(7)
print(result)  

#6. A) palindrome
# no args with return

def palindrome():
    num = 12321
    reverse = 0
    original = num
    
    for i in range(len(str(num))):
        digit =  num % 10
        
        reverse = reverse * 10 + digit
        num = num // 10
    if original == reverse:
            return "Palindrome"
    else:
            return "Not"
result = palindrome()
print(result)

# 6,B) no args without return

def palindrome():
    num = 12321
    reverse = 0
    original = num
    
    for i in range(len(str(num))):
        digit =  num % 10        
        reverse = reverse * 10 + digit
        num = num // 10
    if original == reverse:
            print( "Palindrome")
    else:
            print("Not")
palindrome()

# 6.C) args with returns 
def palindrome(num):
    
    reverse = 0
    original = num
    
    for i in range(len(str(num))):
        digit =  num % 10
        
        reverse = reverse * 10 + digit
        num = num // 10
    if original == reverse:
            return "Palindrome"
    else:
            return "Not"
result = palindrome(121)
print(result)

# 6.D) args without returns 
def palindrome(num):
    
    reverse = 0
    original = num
    
    for i in range(len(str(num))):
        digit =  num % 10
        
        reverse = reverse * 10 + digit
        num = num // 10
    if original == reverse:
            print("Palindrome")
    else:
            print("Not")
palindrome(123)

#reverse num
# 7.A) No args with returns 

def reverse():
    num = 123
    reverse = 0
    
    for i in range(len(str(num))):
        digit =  num % 10
        
        reverse = reverse * 10 + digit
        num = num // 10
    return reverse 
result = reverse()
print(result)

# 7.B) No args without returns 

def reverse():
    num = 123
    reverse = 0
    
    for i in range(len(str(num))):
        digit =  num % 10
        
        reverse = reverse * 10 + digit
        num = num // 10
    print(reverse) 
reverse()

# 7.C) args with returns 

def reverse(num):
    
    reverse = 0
    
    for i in range(len(str(num))):
        digit =  num % 10
        
        reverse = reverse * 10 + digit
        num = num // 10
    return reverse 
result = reverse(122)
print(result)

# 7.D) args without returns 

def reverse(num):
    
    reverse = 0
    
    for i in range(len(str(num))):
        digit =  num % 10
        
        reverse = reverse * 10 + digit
        num = num // 10
    print(reverse)
reverse(157)

#reverse string
# 8.A) no args with return 

def reverse_str():
    
    text = "Python"

    reverse = ""

    for i in range(len(text)-1, -1, -1):
        reverse = reverse + text[i]

    return reverse

result = reverse_str()
print(result)

# 8.B) no args without return 

def reverse_str():
    text = "Java"
    reverse = ""
    
    for i in range(len(text) -1 , -1 ,-1 ):
        
        
        reverse = reverse + text[i]
        
    print(reverse)
reverse_str()        

# 8.C)args with return 

def reverse_str(text):

    reverse = ""

    for i in range(len(text)-1, -1, -1):
        reverse = reverse + text[i]

    return reverse

result = reverse_str("coding")
print(result)

# 8.D) args without return 

def reverse_str(text):
    reverse = ""
    
    for i in range(len(text) -1 , -1 ,-1 ):
        reverse = reverse + text[i]
    print(reverse)
reverse_str("java") 

# count_vowels
# 9.A) no args with return

def count_vowels():
    text = "Education"
    vowel = ["a","e","i","o","u"]
    count = 0
    
    for i in range(len(text)):
        if text[i].lower() in vowel:
            count = count + 1
    return count
result = count_vowels()    
print(result)
    
# 9.B) no args without return

def count_vowels():
    text = "Education"
    vowel = ["a","e","i","o","u"]
    count = 0
    
    for i in range(len(text)):
        if text[i].lower() in vowel:
            count = count + 1
    print(count)
count_vowels() 

# 9.C) args with return

def count_vowels(text):
   
    vowel = ["a","e","i","o","u"]
    count = 0
    
    for i in range(len(text)):
        if text[i].lower() in vowel:
            count = count + 1
    return count
result = count_vowels("class")    
print(result)   
    
# 9.D) args without return

def count_vowels(text):
    
    vowel = ["a","e","i","o","u"]
    count = 0
    
    for i in range(len(text)):
        if text[i].lower() in vowel:
            count = count + 1
    print(count)
count_vowels("Educational")     
    
#Count_digit

#10.A) no args with return

def count_digit():
    
    digit = 12345
    count = 0
    for i in range(len(str(digit))):
        count = count + 1
    return count
result = count_digit()
print(result)
        
#10.B) no args without return

def count_digit():
    
    digit = 12345
    count = 0
    for i in range(len(str(digit))):
        count = count + 1
    print(count)
count_digit()


#10.C )args with return

def count_digit(digit):
    count = 0
    for i in range(len(str(digit))):
        count = count + 1
    return count

result = count_digit(567)
print(result)

        
#10.D) args without return

def count_digit(digit):
 
    count = 0
    for i in range(len(str(digit))):
        count = count + 1
    print(count)
count_digit(9876)

                