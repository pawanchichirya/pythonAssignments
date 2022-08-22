""""
Write a python script to check whether a given number is positive or non-positive
"""
num=int(input("Enter a number: "))
if(num>0):
  print("positive")
else:
  print("non positive")

"""
Write a python script to check whether a given number is divisible by 5 or not
"""
num=int(input("Enter a number: "))
if(num%5==0):
  print("Divisible by 5")
else:
  print("Not Divisible by 5")

"""
Write a python script to check whether a given number is even or odd
"""
num=int(input("Enter a number: "))
if(num%2==0):
  print("Even number")
else:
  print("Odd number")

"""
Write a python script to print greater between two numbers. Print number only once
even if the numbers are the same.
"""
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
if(num1>num2):
  print(num1)
elif(num1==num2):
  print(num1)
else:
  print(num2)

"""
Write a python script to print two given words in dictionary order
"""
word1=input("Enter word1: ")
word2=input("Enter word2: ")
if(word1>word2):
  print(word2,word1,sep=" ")
else:
  print(word1,word2,sep=" ")

"""
Write a python script to check whether a given number is a three digit number or not.
"""
num=int(input("Enter a number: "))
if num>=100 and num<=999:
  print("It's a 3 digit number")
else:
  print("It's not a 3 digit number")

"""
Write a python script to check whether a given number is positive, negative or zero.
"""
num=int(input("Enter a number: "))
if(num>0):
  print("positive")
elif(num<0):
  print("non positive")
else:
  print("it's a zero")

"""
Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots
"""
a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))
determinant=(b**2)-(4*a*c)
if determinant>0:
  print("Roots are real and distinct")
elif determinant==0:
  print("Roots are real and equal")
else:
  print("Imaginary roots")

"""
Write a python script to check whether a given year is a leap year or not.
"""
year=int(input("Enter a year: "))
if (year%400==0) or ((year%4==0) and (year%100!=0)):
  print("Leap year")
else:
  print("Not a Leap year")

"""
Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same.
"""
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
num3=int(input("Enter num3: "))
if num1>num2 and num1>num3:
  print(num1)
elif num2>num3:
  print(num2)
else:
  print(num3)

"""
Write a python script to take the month value in numeric format and display the
number of days in it.
"""
month=int(input("Enter a month: "))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
  print("31")
elif month==2:
  print("28/29")
else:
  print("30")

"""
Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part
"""
num=complex(input("Enter a valid complex number: "))
if num.real>num.imag:
  print(num.real)
else:
  print(num.imag)