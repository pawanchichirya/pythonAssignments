#Write a python script to print all Prime numbers between two given numbers (both values inclusive)
import math
start=int(input("Enter start value: "))
end=int(input("Enter end value: "))
for i in range(start,end+1):
    if i==1:
        continue
    if i==2:
        print(i)
    for j in range(2,math.ceil(math.sqrt(i))+1):
        if i%j==0:
            break
    else:
        print(i)