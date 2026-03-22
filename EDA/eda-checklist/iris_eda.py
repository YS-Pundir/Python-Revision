# importing the needed libraries 
import pandas as pd 
import plotly.express as px 

# loading the Dataset using pandas dataframes

data=pd.read_csv("iris.csv")

# Step 1 : Inspecting dataset Structure  using df.info() method of pandas libraris 
print("The Datastructure of the Dataset is : ")
print(data.info())
print("The Statistical Summary of the Dataset is : ")
print(data.describe())

    # Observation : There are total  150 entries and 5 columns

# Step 2 : Checking for column information and missing values using data.describe() and data.isnull().sum()
print("-"*60)
print("The Statistical Summary of the Dataset is : ")
print(data.describe())
print("Checking for the null values in dataset : ")
print(data.isnull().sum())
    # Obsevation : 4 out of 5 columns have numerical data , and there is no null values

# Step 3 : Ananlysing Distribution of feature using the Histogram Chart
fig=px.histogram(
    data,
    x="petal_length",
    title="Distribution of Pental Length "
)

fig.show()
    # Observation : The Dataset is highly dense between 1.3 and 1.7 values on pental length , and zero between 2.2 and 2.8

# Step 4 : Identifing the Possible Outliers in dataset using the box Chart
fig=px.box(
    data,
    y=["sepal_length","petal_length"],
    title="Idnetifing the Possible outliers"
)
fig.show()
    # Observation : The Dataset has no outliers for sepal_length,petal_length

# Step 5 : Analysing the relation between variable using the correlation heatmap
crr=data[["petal_length","petal_width"]].corr(numeric_only=True)
print(crr)

fig=px.imshow(
    crr,
    title="Corelation bitween petal length and petal width"
)
fig.show()
    #Observation : both of these varibale are directcly propoitonal to each other at the rate of 0.96(approx) . 

# Conclusional Insight : The high correlation (0.96) between petal length and petal width indicates that these two features are nearly redundant, making them the most reliable "fingerprints" for distinguishing between species.