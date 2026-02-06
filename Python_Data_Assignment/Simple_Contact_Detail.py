Contact_Details={
    "Yuvraj Singh Pundir ":"+91-17723989608256",
    "Prem Singh":"+91-989673409090",
    "Rana Ajmer Singh":"+91-787878989656",
    "Reena Devi":"+91-80767343432254"

}
print("-"*50)
print("The all Contact Details are :->")
for key,value in Contact_Details.items():
    print(f"Name : {key} -> Phone Number : {value}")
print("-"*50)
name=input("Please enter the name whome you waant to contact : ",)
if name in Contact_Details.keys():
    print("The phone number of requested user is ",Contact_Details[name])
else:
    print("Contact not found !!")




