import pandas as pd 

data={
    "Name":["Yuvraj Singh","Prashant Kumar","Rohit Sharma","Amit Thakur","Akshay Rana","Himanshu Choudhry","Abhishek Pundir","Udit Narayan"],
    "Score":[99,77,48,73,59,82,47,66],
    "Passed":[True,False,False,True,False,True,True,True],
    "Category":["a","d","d","a","d","c","b","a"]
}
df=pd.DataFrame(data)
print("Orignal Dataset : ")
print(df)
print("-"*60)


print("The names of the students , Attempted the examination : ")
print()
print(df["Name"])

print("-"*60)
print("A Small summary of dataset : ")
print()
print(df[["Name","Passed","Category"]])

print("-"*60)
print("First Three column of the dataset : ")
print(df.iloc[0:3])