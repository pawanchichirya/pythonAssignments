#Write a python script to create a String in 3 different possible ways
name="pawan"
age=str(21)
institute='''MySir'g.com'''
print(name,age,institute,sep=" ")

#Write a python script to Get the characters from the start to position 5
str1="iNeuron"
print(str1[:6])

#Write a python script to Get the characters from position 2 to position 5 
str1="Hello Learners"
print(str1[2:6])

#Write a python script to demonstr1ate String Concatenation adding space in between ( Given Strings a=”Learning” b=”Python” )
a="Learning"
b="Python"
print(a+" "+b)

#Write a python script to get the count of total number of characters in String
a="iNeuron"
print(len(a))

#Write a python script to reverse a String. (“iNeuron”)
str1="iNeuron"
print(str1[::-1])

#Write a python script to determine whether a string contains a specific substring.
str1="we will get back to you soon"
substr="gett"
if substr in str1:
    print(True)
else:
    print(False)

#Write a python script to check if a string contains only numbers.
str1="hruegjg84ytiu8"
print(str1.isdigit())

#Write a python script to check if a string contains only characters of the alphabet.
str1="fgfgvfbvf"
print(str1.isalpha())

#Write a python script to convert an integer to a string.
age=str(21)
print(type(age))