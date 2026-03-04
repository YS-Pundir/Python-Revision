# 🔹 Sample Data (5–10 Rows)

import pandas as pd
import numpy as np

# Creating sample dataset
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

print(df)

print("-"*60)
missing_values=df.isnull().sum()
print("The summary of missing values in dataframe is something like that : ")
print(missing_values)


print("-"*60)
df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
print("The dataframe After filling the misssing values : ")
print(df)
