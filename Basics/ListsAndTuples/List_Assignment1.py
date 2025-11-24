#taking elements of list from user and then doing some operations
list=[]
n=int(input("enter the length of the list : ",))
for i in range (n):
    num=int(input("enter the number : ",))
    list.append(num)

#function to print the sum of every element of list
def additon():
    sum=0
    for i in list:
        sum+=i
    return sum


    
    
    
