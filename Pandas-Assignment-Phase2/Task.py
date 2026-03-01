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

print("-"*60)
df.index=[1001,1002,1003,1004,1005,1006,1007,1008]
print("Printing name of the student by  id of student :-")
print(df.loc[1004,"Name"])
print("Printing the First three rows of Datasetv with updated index : " )
print(df.loc[1001:1005])