#Write a python script to store multiple items in a single variable ( Items are “Java”,“Python”, “SQL”, “C” ) using list
lst=["Java","Python","SQL","C"]
print(lst)

#Write a python script to get the data type of a list.
print(type(lst))

#Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])
mylist = ["Java", "C", "Python"]
print(mylist[-1])

#Write a python script to Change the values "SQL" and "Reactnative" with the values "NoSQL" and "Flutter" (List is this list = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]
list = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]
idx1=list.index("SQL")
list[idx1]="NoSQL"
idx2=list.index("Reactnative")
list[idx2]="Flutter"
print(list)

#Write a python script to add an item to the end of the list (item “Python”. (mylist = ["Java", "SQL", "C", "Reactnative"]
mylist =["Java", "SQL", "C", "Reactnative"]
mylist.append("Python")
print(mylist)

#Write a python program to append elements from another list to the current list.
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"] 
print(firstlist+secondlist)

#Write a python program to Print all items by referring to their index number 
lst=["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
for i in range(len(lst)):
    print(i,lst[i],sep=" ")

#Write a python program to sort the list alphanumerically – this
list = ["Java", "SQL","C", "Reactjs", "Javascript", "Python"]
print(sorted(list))

#Write a Python script to create a list of city names taken from the user.
n=int(input("How many cities you are going to enter: "))
lst=[]
for i in range(n):
    lst.append(input())
print(lst)

#Write a Python script to create a list, where each element of the list is a digit of a given number.
n=int(input("Enter a number: "))
print([i for i in str(n)])