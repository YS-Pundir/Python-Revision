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

#now programe to find the percentage of the student 

list1=[]#taking a blank list

a=Students["Course"]["Subject"]["Major"]["Physics"]["Marks"]
list1.append(a)
b=Students["Course"]["Subject"]["Major"]["Chemistry"]["Marks"]
list1.append(b)
c=Students["Course"]["Subject"]["Major"]["Mathematics"]["Marks"]
list1.append(c)
d=Students["Course"]["Subject"]["Minor"]["Physical Education"]["Marks"]
list1.append(d)
e=Students["Course"]["Subject"]["Minor"]["English"]["Marks"]
list1.append(e)
#printin the result of appended list
print("the list of marks are",list1)

#adding all the marks
sum=0
for i in list1:
    sum+=i
#printing the percentage
print("the percentage of marks being obtained by student is : ",(sum/500)*100)

#updating the contact information
Students["Contact Details"]["Phone Number"]=919896077777
Students["Contact Details"]["Email Address"]="yuvrajpundir2555@gmail.com"
print("The contact details of a student is ",Students["Contact Details"])

    
    





