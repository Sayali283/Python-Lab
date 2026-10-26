#Perform data cleaning, preprocessing, filtering, aggregation, and exploratory data analysis using the Pandas library.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create a sample dataset
data = {
    "Name": [
        "Amit", "Priya", "Rahul", "Sneha",
        "amit", "Neha", "Karan", "Priya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "IT", "HR", "Finance", "HR"
    ],
    "Age": [21, 22, np.nan, 24, 21, 23, 25, 22],
    "Salary": [
        45000, 50000, 55000, np.nan,
        45000, 48000, 60000, 50000
    ],
    "Performance": [85, 90, 78, 88, 85, np.nan, 92, 90]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# 2. Inspect the dataset
print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# 3. Data cleaning
# Remove duplicate records
df = df.drop_duplicates()

# Standardize text
df["Name"] = df["Name"].str.strip().str.title()
df["Department"] = (
    df["Department"].str.strip().str.title()
)

# Fill missing numerical values with column medians
for column in ["Age", "Salary", "Performance"]:
    df[column] = df[column].fillna(df[column].median())

# Convert data types
df["Age"] = df["Age"].astype(int)
df["Salary"] = df["Salary"].astype(float)

print("\nCleaned Dataset:")
print(df)

# 4. Data preprocessing
# Create a new column
df["Annual_Salary"] = df["Salary"] * 12

# Categorize performance
df["Performance_Level"] = pd.cut(
    df["Performance"],
    bins=[-1, 60, 80, 100],
    labels=["Low", "Medium", "High"]
)

print("\nPreprocessed Dataset:")
print(df)

# 5. Filtering
print("\nEmployees with Salary above 48000:")
print(df[df["Salary"] > 48000])

print("\nIT Department Employees:")
print(df[df["Department"] == "It"])

print("\nEmployees aged 22 or older with performance >= 85:")
filtered_df = df[
    (df["Age"] >= 22) &
    (df["Performance"] >= 85)
]
print(filtered_df)

# 6. Aggregation
print("\nDepartment-wise Statistics:")
department_summary = df.groupby("Department").agg(
    Employee_Count=("Name", "count"),
    Average_Salary=("Salary", "mean"),
    Maximum_Salary=("Salary", "max"),
    Average_Performance=("Performance", "mean")
).round(2)

print(department_summary)

print("\nOverall Statistics:")
print(df[["Age", "Salary", "Performance"]].describe())

# 7. Exploratory Data Analysis (EDA)
print("\nCorrelation Matrix:")
print(
    df[["Age", "Salary", "Performance"]].corr().round(2)
)

# Salary distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Salary"], bins=5, kde=True)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Department-wise average salary
plt.figure(figsize=(8, 5))
sns.barplot(
    data=df,
    x="Department",
    y="Salary",
    hue="Department",
    legend=False
)
plt.title("Salary by Department")
plt.tight_layout()
plt.show()

# Correlation heatmap
plt.figure(figsize=(7, 5))
sns.heatmap(
    df[["Age", "Salary", "Performance"]].corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# 8. Export cleaned data
df.to_csv("cleaned_employee_data.csv", index=False)
department_summary.to_csv("department_summary.csv")

print("\nAnalysis complete.")
print("Cleaned data saved to cleaned_employee_data.csv")
print("Department summary saved to department_summary.csv")
