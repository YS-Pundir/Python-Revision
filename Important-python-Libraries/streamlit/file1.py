import streamlit as st
st.title("Programing Language store")
st.subheader("All language available")
st.write("wellcome to my first interavtive app")
choice=st.selectbox("Choose any of the lanuuages  : ",["Python","Java","C++","Javascript","HTML","CSS"])
st.write(f"{choice} has been choosen")
st.success("You are ready to do programing")
