

def greeting(name):
    return f"Hello {name} "

def result(list):
    sum=0
    for i in list:
        sum+=i

    return len(list),sum/len(list)
    



def Pass_Fail_checker(average):
    if  average >50:
        return "Pass"
    else:
        return "Fail"
    

def main():
    name=input("Enter the name of student : ",)
    list=[]
    n=int(input("Enetr the no of subject : ",))
    for i in range(n):
        marks=int(input("Enter the marks in the subject : "))
        list.append(marks)

    

    print(greeting(name))

    no_of_subjects,average=result(list)

    print(f"Subjects :{no_of_subjects}")
    print(f"Average Score : {average}")

    print("Reesult : ",Pass_Fail_checker(average))

if __name__ ==main():
    main()
