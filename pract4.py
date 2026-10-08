# Program to calculate total marks and grade

name = input("Enter student name: ")

total = 0

# Loop to enter marks of 3 subjects
for i in range(1, 4):
    marks = int(input("Enter marks of subject " + str(i) + ": "))
    total = total + marks

# Calculate percentage
percentage = total / 3

print("\n----- Student Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

# Decision-making
if percentage >= 75:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 50:
    print("Grade: C")
elif percentage >= 35:
    print("Grade: D")
else:
    print("Grade: F")