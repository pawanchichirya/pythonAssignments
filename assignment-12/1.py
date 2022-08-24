#Write a python script to reverse a number.
n=int(input("Enter the num: "))
reversed=0

while(n>0):
    digit=n%10
    reversed=reversed*10+digit
    n//=10
print(reversed)
