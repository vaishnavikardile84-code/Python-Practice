id = 21

if id % 2 == 0:
    print("Even")
else:
    print("Odd")
    
num = -22

if num > 0 :
    print("Positive")
elif num < 0:
    print("Negative")   
else:
    print("Zero") 
    
a = 1234
reverse = 0
i = 0
while i  < a:
    digit = a % 10
    reverse = reverse * 10 + digit
    a = a // 10
    
print(reverse)
a = int(input("Enter a number: "))

ori = a
reverse = 0

while a > 0:
    d = a % 10
    reverse = reverse * 10 + d
    a = a // 10

if ori == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
    # -----------------------------------------------
    
A = [1, 6, 8, 9, 2, 5, 3]

i = 0

while i < len(A):

    num = A[i]

    if num <= 1:
        print("Not Prime:", num)

    else:
        j = 2
        is_prime = True

        while j < num:
            if num % j == 0:
                is_prime = False
                break

            j += 1

        if is_prime:
            print("Prime:", num)
        else:
            print("Not Prime:", num)

    i += 1


 

      
            
    