#Write a python script to calculate LCM of two numbers
num1=int(input("Enter the num1: "))
num2=int(input("Enter the num2: "))
n1=num1
n2=num2
gcd=1

while(num1!=num2):
    if(num1>num2):
        num1=num1-num2
    else:
        num2=num2-num1
    
gcd=num1
lcm=(n1*n2)//gcd
print(lcm)