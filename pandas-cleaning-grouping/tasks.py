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
print("Orignal DataFrame : ")
print(df)

print("-"*60)
missing_values=df.isnull().sum()
print("The summary of missing values in dataframe is something like that : ")
print(missing_values)


print("-"*60)
df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
print("The dataframe After filling the misssing values : ")
print(df)

print("-"*60)
df.drop(columns=["Temporary_Notes"],inplace=True)
print("Dataframe after deleting the temprary file column from df : ")
print(df)

print("-"*60)
df.rename(columns={
    "Salary":"Anuall_Salary",
    "Employee":"Employee_Name"
},inplace=True)
print("DataFrame after changing names of columns : ")
print(df)

print("-"*60)
summary=df.groupby("Department").agg({
    "Anuall_Salary":"mean",
    "Employee_Name":"count"

})

print("Summary DataFrame : ")
print(summary)