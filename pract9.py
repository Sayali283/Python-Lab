#Develop Python applications using built-in modules and libraries such as NumPy and Pandas to perform statistical analysis, data manipulation, randomization, and utility-based operations.
import numpy as np
import pandas as pd
import random

students = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Maths": [85, 92, 67, 78, 88],
    "Science": [80, 95, 72, 84, 90],
    "English": [75, 89, 70, 82, 86]
})

subjects = ["Maths", "Science", "English"]

students["Average"] = students[subjects].mean(axis=1)
students["Total"] = students[subjects].sum(axis=1)
students["Grade"] = np.select(
    [
        students["Average"] >= 90,
        students["Average"] >= 80,
        students["Average"] >= 70
    ],
    ["A", "B", "C"],
    default="D"
)

print("Student Performance:")
print(students)

print("\nClass Average:", students["Average"].mean())
print("Highest Average:", students["Average"].max())
print("Lowest Average:", students["Average"].min())

print("\nTop Performer:")
print(students.loc[students["Average"].idxmax()])

print("\nRandom Student:")
print(students.iloc[random.randrange(len(students))])

students.to_csv("student_analysis.csv", index=False)
print("\nResults saved to student_analysis.csv")

import numpy as np
import pandas as pd
import random

students = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Maths": [85, 92, 67, 78, 88],
    "Science": [80, 95, 72, 84, 90],
    "English": [75, 89, 70, 82, 86]
})

subjects = ["Maths", "Science", "English"]

students["Average"] = students[subjects].mean(axis=1)
students["Total"] = students[subjects].sum(axis=1)
students["Grade"] = np.select(
    [
        students["Average"] >= 90,
        students["Average"] >= 80,
        students["Average"] >= 70
    ],
    ["A", "B", "C"],
    default="D"
)

print("Student Performance:")
print(students)

print("\nClass Average:", students["Average"].mean())
print("Highest Average:", students["Average"].max())
print("Lowest Average:", students["Average"].min())

print("\nTop Performer:")
print(students.loc[students["Average"].idxmax()])

print("\nRandom Student:")
print(students.iloc[random.randrange(len(students))])

students.to_csv("student_analysis.csv", index=False)
print("\nResults saved to student_analysis.csv")

import numpy as np
import pandas as pd
import random

students = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Maths": [85, 92, 67, 78, 88],
    "Science": [80, 95, 72, 84, 90],
    "English": [75, 89, 70, 82, 86]
})

subjects = ["Maths", "Science", "English"]

students["Average"] = students[subjects].mean(axis=1)
students["Total"] = students[subjects].sum(axis=1)
students["Grade"] = np.select(
    [
        students["Average"] >= 90,
        students["Average"] >= 80,
        students["Average"] >= 70
    ],
    ["A", "B", "C"],
    default="D"
)

print("Student Performance:")
print(students)

print("\nClass Average:", students["Average"].mean())
print("Highest Average:", students["Average"].max())
print("Lowest Average:", students["Average"].min())

print("\nTop Performer:")
print(students.loc[students["Average"].idxmax()])

print("\nRandom Student:")
print(students.iloc[random.randrange(len(students))])

students.to_csv("student_analysis.csv", index=False)
print("\nResults saved to student_analysis.csv")
