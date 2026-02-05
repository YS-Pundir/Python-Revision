name=input("Enter the name of student : ",)
list=[45,76,99,100,99.8,67]

def greeting(name):
    return f"Hello {name} "

def result(list):
    sum=0
    for i in list:
        sum+=i

    return len(list),sum/len(list)
    

no_of_subjects,average=result(list)

def Pass_Fail_checker():
    if  average >50:
        return "Pass"
    else:
        return "Fail"
    

