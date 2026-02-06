user1={
    "Name":"Yuvraj Singh",
    "Score":[99,78,96,99],
    "Role":{"AI Engineer","Build Models","Deploy The Mode","Admin"}
}

user2={
    "Name":"Himanshu Sharma",
    "Score":[78,67,98,67],
    "Role":{"Data Analyst","Analyse Data","Story Telling"}
}

user3={
    "Name":"Himanshu Rana",
    "Score":[66,88,33,98],
    "Role":{"It","Resolve IT Problems","Build IT Agile"
}}

user4={
    "Name":"Prince Dhull",
    "Score":[88,66,99,67],
    "Role":{"Finance","Moniter the money","Make Strategies"}
    }
list_of_users=[user1,user2,user3,user4]

def avg_Score(list):
    
    sum=0
    for i in list :
        for j in i["Score"]:
            sum+=j
        i[f"Average Score"]=sum/len(i["Score"])

        
    return list

def role_checker(role):
    if "Admin" in role:
        return True
    else:
        return False
    
def main():

    avg_Score(list_of_users)

    for i in list_of_users:
        
        print(f"Name of user: {i["Name"]} , Average Score of user: {i["Average Score"]} , Admin role given : {role_checker(i["Role"])}")

if __name__==main():
    main()

