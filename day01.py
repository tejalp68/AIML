'''
Name : Tejal Dadaji Pagar
Cohort : AIML & TEP cohort 2026
Day : Sunday
Date : 09/08/2026
Description :This program covers variables & data types, typecasting(str to int, int to str, and using pandas to_numeric), 
string indexing/slicing, list indexing/slicing,dict,tuple,if-else conditions to check student attendance, and for loop & while loop examples.
'''
# Variable  an Data types
x = 10 #int
y = 20 #int
print(x+y)

#typecasting

x="123"
x=int(x)
print(type(x)) #converting string to int
num =123
str1 =str(num)
print(str1)
print(type(str1))

import pandas as pd
num = "123"
str1 = pd.to_numeric(num  )
print(str1) 
print(type(str1))

#String indexing and slicing 
str ="Hello this is a string in Python"

print(str[0:7])
print(str[2:])
print(str[16:22])

#List  
lst=[1,'abc','sabnam',123]

#list indexing and slicing 
print(lst[1])
print(lst[-1])
print(lst[0:])
print(lst[::-1])

#Dict 
dict1 ={"Stud1":"Arjun","Stud2":"Rahul","Stud3":"Riya"}
print(dict1.keys())
print(dict1.items())
print(dict1.values())
dict1["Stud4"]="Rani" #--->adding new ele
print(dict1)

# Tuple
tup1 =("hello","this","is","python","tuple")
print(tup1.index("hello"))
print(tup1.count("python"))

# Conditional Statements
#if else block

Students =["Ahan","Riya","Aryan","Khushi","Mahima","sunil","Neeta"]
Attendance =["Ahan","Aryan","Khushi","mahima","Neeta"]

stud = input ("Enter Student Name : ").title()

if stud in Students:
    if stud not in Attendance:
        print(stud,"is Not present")
    else:
        print(stud,"is Present")

else:
    print("This Student is not from class")

## if elif else
# Problem Statement: Movie Ticket Pricing System .A cinema charges ticket prices based on age, day of the week, and whether the person is a student.
# Rules:
# - If age is less than 5 → ticket is FREE
# - If age is between 5 and 12 (inclusive) → ticket price is ₹100
# - If age is between 13 and 59 (inclusive):
# - If the day is "Monday" or "Tuesday" → price is ₹150 (weekday discount)
# - Else if the person is a student → price is ₹180
# - Else → price is ₹250
# - If age is 60 or above → ticket price is ₹120 (senior citizen discount)


age = int(input("Enter your Age :"))
day = input("Enter Day :").title()
is_student = input("Are you Student (yes/no) :").lower()

if age < 5:
    print("Ticket is Free!!!yayy!!!")
elif age >= 5 and age <= 12:
    print ("Ticket Price :₹150")
elif age >= 13 and age <= 59:
    if day == "Monday" or  day == "Tuesday":
        print("Ticket Price is : ₹150(Weekday Discount)")
    elif is_student == "yes" :
        print("Ticket Price is :₹180") 
    else:
         print("Ticket Price : ₹250")
elif age    >= 60:
    print("Ticket Price :₹120")

# Loop 
# For Loop 
for i in range (0,5):
    print(i)


# While Loop
i = 1
while i < 5:
    print(i)
    i+= 1   