#Write a python script to calculate HCF of two numbers
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
    
hcf=num1
print(hcf)