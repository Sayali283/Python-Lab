# Program to calculate student result and grade

name = input("Enter student name: ")

maths = float(input("Enter marks in Maths: "))
science = float(input("Enter marks in Science: "))
english = float(input("Enter marks in English: "))

# Calculate total and percentage
total = maths + science + english
percentage = total / 3

print("\n----- Student Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

# Check result and grade
if maths >= 35 and science >= 35 and english >= 35:
    print("Result: PASS")

    if percentage >= 75:
        print("Grade: A")
    elif percentage >= 60:
        print("Grade: B")
    elif percentage >= 50:
        print("Grade: C")
    else:
        print("Grade: D")

else:
    print("Result: FAIL")
    print("Grade: F")

# Check whether student has scored distinction
if percentage >= 75 and maths >= 75 and science >= 75:
    print("Distinction: Yes")
else:
    print("Distinction: No")