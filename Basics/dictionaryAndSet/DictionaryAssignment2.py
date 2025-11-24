#making  a Student management system
Students={
    "Name":"Yuvraj Singh Pundir",
    "Roll NUmber":39084376,
    "Course":{
        "Subject":{
            "Major":{
                "Physics":{"Teacher":"Rajesh Sharma","Marks":82},
                "Chemistry":{"Teacher":"Pardeep","Marks":83},
                "Mathematics":{"Teacher":"Amit Setia","Marks":93}
            },
            "Minor":{
                "English":{"Teacher":"Dinesh Sharma","Marks":81},
                "Physical Education":{"Teacher":"Sushma Mehla","Marks":99}

            },

        },
        "Assessment":{
            "Discipline":{"Marks":100},
            "Punctuality":{"Marks":99}
        },

    },
    "Parent Name":{
    "Mother Name":"Mrs. Sudesh ","Father Name":"Mr. Satbir Singh"
        
        },
    "Contact Details":{"Phone Number":+49177231111,"Address":"Berlin Alxenderplatz"}

    }
#Printing the  complete dictionary
print(Students)
#printing just the major subjects
print("the major subjects being studied by a student : ",list(Students["Course"]["Subject"]["Major"].keys()))





