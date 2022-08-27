#Write a Python script to create a list of first N natural numbers.
n=int(input("Enter the value of n: "))
lst=[i for i in range(1,n+1)]
print(lst)

#Write a Python script to create a list of first N odd natural numbers.
n=int(input("Enter the value of n: "))
lst=[i for i in range(1,2*n+1) if i%2!=0]
print(lst)

#Write a Python script to create a list of first N even natural numbers.
n=int(input("Enter the value of n: "))
lst=[i for i in range(1,2*n+1) if i%2==0]
print(lst)

#Write a Python script to find the greatest number in a given list of numbers.
n=int(input("How many numbers you are going to enter: "))
lst=[]
for i in range(n):
    lst.append(int(input()))
print(max(lst))

#Write a Python script to find the smallest number in a given list of numbers.
n=int(input("How many numbers you are going to enter: "))
lst=[]
for i in range(n):
    lst.append(int(input()))
print(min(lst))

#Write a Python script to calculate the sum of elements in a given list of numbers.
n=int(input("How many numbers you are going to enter: "))
lst=[]
for i in range(n):
    lst.append(int(input()))
print(sum(lst))

#Write a Python script to remove all non int values from a list.
lst=["pawan",22,55,56.7,3+4j,True,"tirumala"]
lst2=[i for i in lst if type(i)==int]
print(lst2)

#Write a Python script to print distinct elements along with their frequencies of occurrence in the list.
n=int(input("How many numbers you are going to enter: "))
lst=[]
for i in range(n):
    lst.append(int(input()))
lst2=sorted(lst)
cached_lst=[]
for i in range(len(lst2)):
    if lst2[i] not in cached_lst:
        cached_lst.append(lst2[i])
    else:
        continue
    print(lst[i],lst.count(lst[i]))

#Write a Python script to print indices of all occurrences of a given element in a given list.
n=int(input("How many numbers you are going to enter: "))
lst=[]
for i in range(n):
    lst.append(int(input()))
term=int(input("Enter the number you want to search: "))
lst2=[i for i in range(len(lst)) if lst[i]==term]
print(lst2)

#Write a python script to sort a list.
n=int(input("How many numbers you are going to enter: "))
lst=[]
for i in range(n):
    lst.append(int(input()))
print(sorted(lst))