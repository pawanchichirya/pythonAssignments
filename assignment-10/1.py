#Write a python script to print MySirG N times on the screen
n=int(input("enter the value of n: "))
for i in range(n):
    print("MySirG")

#Write a python script to print first N natural numbers
n=int(input("enter the value of n: "))
for i in range(1,n+1):
    print(i)

#Write a python script to print first N natural numbers in reverse order
n=int(input("enter the value of n: "))
for i in range(n,0,-1):
    print(i)

#Write a python script to print first N odd natural numbers
n=int(input("enter the value of n: "))
for i in range(1,2*n,2):
    print(i)

#Write a python script to print first N odd natural numbers in reverse order
n=int(input("enter the value of n: "))
for i in range(2*n-1,0,-2):
    print(i)

#Write a python script to print first N even natural numbers
n=int(input("enter the value of n: "))
for i in range(2,2*n+1,2):
    print(i)

#Write a python script to print first N even natural numbers in reverse order
n=int(input("enter the value of n: "))
for i in range(2*n,1,-2):
    print(i)

#Write a python script to print squares of first N natural numbers
n=int(input("enter the value of n: "))
for i in range(1,n+1):
    print(i**2)

#Write a python script to print cubes of first N natural numbers
n=int(input("enter the value of n: "))
for i in range(1,n+1):
    print(i**3)

#Write a python script to print first 10 multiples of Nq
n=int(input("enter the value of n: "))
for i in range(1,11):
    print(n*i)