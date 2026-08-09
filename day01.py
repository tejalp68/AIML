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
