#Write Python programs to demonstrate the use of variables and data types .
Name=" Sayali!"#str
roll_no=27#int
Sch=1.200#float
is_student=True#bool
print(f"Student Name:{Name}, Type:{type(Name)}")
print(f"Student Roll No.:{roll_no}, Type:{type(roll_no)}")
print(f"Student Scholership :{Sch}, Type:{type(Sch)}")
print(f" Check Student:{is_student}, Type:{type(is_student)}")
#Type Conversion
roll_float=float(roll_no)
print(f"Roll no. conversion in float:{roll_float}, Type:{type(roll_float)}")

#input / output operations, arithmetic operators.
num1=int(input("Enter 1st No.:"))
num2=int(input("Enter 2nd No.:"))
#Addition
print("Addition of NO.:",num1+num2)
#Substraction
print("Substraction of NO.:",num1-num2)
#Munltiplication
print("Multiplication of NO.:",num1*num2)
#Division
print("Division of NO.:",num1/num2)
#Floor Division
print("Floor Division of NO.:",num1//num2)
#Modulas
print("Modulas of NO.:",num1%num2)
#Exponential
print("Exponential of NO.:",num1**num2)
