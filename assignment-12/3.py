#Write a python script to print all Prime numbers under 100
#Write a python script to check whether a given number is Prime or not
import math
for i in range(2,101):
    if i==2:
        print(i)
    for j in range(2,math.ceil(math.sqrt(i))+1):
        if i%j==0:
            break
    else:
        print(i)