#Book store inventory management'
Book_store={
    "Name":"Ram Book Store",
    "Location":"Berlin Freidrichtasse 14",
    "inventory":{
        "fiction":{
            "1984":{"price":15.99,"stock":16,"Auther":"Gautham Manni"},
            "Sex Education":{"price":17.6,"stock":30,"Auther":"Yuvraj Singh"}
        },
        "Non fiction":{
            "Story of my Life":{"price":999,"Auther":"Annie bassant","Stock":"limited"},
            "Experiment of my life":{"price":118,"Auther":"Gandhi","stock":18}

        },
    
    },
    "Employees ":{"Bob","Adolf","Michel","Willium"},
    "Founder":{"Yuvraj Singh Pundir"},
    "Year of establishment":1986
}
#printing the whole dictionary
print(Book_store)
#printing a specific key
print("accessing the specific key to print its value",Book_store["inventory"])
#printing all book categories available 
print("printing all book categories that are available",list(Book_store["inventory"].keys()))
#printing price of 1984
print("the price of 1984 is :",Book_store["inventory"]["fiction"]["1984"]["price"])
