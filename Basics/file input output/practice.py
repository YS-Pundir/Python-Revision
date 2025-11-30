#replacing java with python
with open("sample.txt","r") as f :
    data=f.read()
#creating aanother data in which the words will be replaced in the older one
new_data=data.replace("Java","Python")
print(new_data)

