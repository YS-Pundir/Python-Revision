contact={
    "name":"Yuvraj Singh Pundir",
    "Backgorund":"Indian",
    "Contact Details":("989862684","282428642"),
    "Emails":{"Personal":"yuvrajsingh@gmail.com","Work":"pundirdev@tesla.de"},
    "Job":{"develop the sutomation for the vehicle","Connect the becked to the ai automation"},#in sets , order depend upon the hash items
    "Working Days":[["Monday","tuesday","wednesday","Friday"],["January to december"]]
    


}

for key,value in contact.items():#item() is the method to store the keys and the value of the dictionary
    print(f" {key} : {value}")