age=int(input("Please enter your age : ",))
id_available=input("Do you have an id (Yes/No) : ",)

if age>=18 and id_available=="Yes":
    print("Entry Allowed")

else:
    print("Entry not allowed")