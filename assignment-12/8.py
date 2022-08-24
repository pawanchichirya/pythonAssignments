#Write a python script to print first N terms of a Fibonacci series
n=int(input("Enter the value of n: "))
a=0
b=1
print(a)
for i in range(1,n):
    print(b)
    c=a+b
    a,b=b,c


