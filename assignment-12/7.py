#Write a python script to check whether a given pair of numbers are co-Prime numbers or not.
#numbers are co prime if they have gcd==1 
num1=int(input("Enter the num1: "))
num2=int(input("Enter the num2: "))
gcd=1

while(num1!=num2):
    if(num1>num2):
        num1=num1-num2
    else:
        num2=num2-num1
    
gcd=num1
if gcd==1:
    print("Numbers are co-prime")
else:
    print("Numbers are not co-prime")