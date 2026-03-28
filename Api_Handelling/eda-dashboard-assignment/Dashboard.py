import requests
import pandas as pd 
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st


url="https://jsonplaceholder.typicode.com/posts"

response=requests.get(url)
if response.status_code==200:
    data=response.json()
else:
    print(response.status_code)

df=pd.DataFrame(data)


# Checking th estructure of the data
print("The shape of the dataframe is : ")
print(df.shape)
print("-"*50)
print("Printing the structural summary of data : ")
print(df.info())
print("-"*50)
print("Printing the statistical summary of the data : ")
print(df.describe())

# Cleaning of data
# rename the column from userID to user_id 
# and drop column id 
df=df.rename(columns={
    "userId":"user_id"
})
df=df.drop("id",axis=1)
print("The resulting data :--> ")
print(df)

# Further Cleaning data
# 1. Printing the post per user using the 
Post_per_User=df.groupby("user_id").count()
print("No of Posts by each user : ")
print(Post_per_User)
# Adding  a column of length of each post
df["Post_Length"]=df["body"].apply(len)
print(df)


st.title("Simple Post Dashboard")
st.write("Showing Data")
st.dataframe(df)

st.subheader("Filter by user")
user=st.selectbox("Select User",df["user_id"].unique())
user_df=df[df["user_id"]==user]
st.write(user_df)

st.subheader("Postr Leangth Distribution")
fig=px.histogram(df,x="Post_Length")
st.plotly_chart(fig)