#Write a python script to find next prime number of a given number
n=int(input("Enter the prime number: "))
import math,sys
for i in range(n+1,sys.maxsize):
    for j in range(2,math.ceil(math.sqrt(i))+1):
        if i%j==0:
            break
    else:
        print(i)
        break