#Write a python script to check whether a given number is Prime or not
import math,sys
n=int(input("Enter a num: "))
if n==1:
    print("Neither prime nor composite")
    sys.exit()
if n==2 or n==3:
    print("Prime number")
    sys.exit()

for i in range(2,math.ceil(math.sqrt(n))+1):
    if n%i==0:
        print("Not a prime number")
        break
else:
    print("Prime number")