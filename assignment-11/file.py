#Write a python script to calculate sum of first N natural numbers
n=int(input("enter the value of n: "))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

#Write a python script to calculate sum of squares of first N natural numbers
n=int(input("enter the value of n: "))
sum=0
for i in range(1,n+1):
    sum+=i**2
print(sum)

#Write a python script to calculate sum of cubes of first N natural numbers
n=int(input("enter the value of n: "))
sum=0
for i in range(1,n+1):
    sum+=i**3
print(sum)

#Write a python script to calculate sum of first N odd natural numbers
n=int(input("enter the value of n: "))
sum=0
for i in range(1,2*n,2):
    sum+=i
print(sum)

#Write a python script to calculate sum of first N even natural numbers
n=int(input("enter the value of n: "))
sum=0
for i in range(2,2*n+1,2):
    sum+=i
print(sum)

#Write a python script to calculate factorial of a given number
n=int(input("enter the value of num: "))
fact=1
for i in range(2,n+1):
    fact*=i
print(fact)

#Write a python script to count digits in a given number
n=int(input("enter the value of num: "))
count=0
while(n>0):
    n//=10
    count+=1
print(count)

#Write a python script to calculate sum of digits of a given number
n=int(input("enter the value of num: "))
sum=0
while(n>0):
    sum+=n%10
    n//=10
print(sum)

#Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)
n=int(input("enter the value of num: "))
bin=""
while(n>0):
    if n%2==0:
        bin+="0"
    else:
        bin+="1"
    n//=2
print(bin[::-1])

#Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)
n=int(input("enter the value of num: "))
oct=""
while(n>0):
    oct+=str(n%8)
    n//=8
print(oct[::-1])