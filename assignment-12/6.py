#Write a python script to print first N prime numbers
import math,sys
n=int(input("Enter the value of n: "))
count=1
for i in range(2,sys.maxsize):
    if count==n:
        sys.exit()
    if i==2:
        print(i)
    for j in range(2,math.ceil(math.sqrt(i))+1):
        if i%j==0:
            break
    else:
        count+=1
        print(i)
    