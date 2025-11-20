#This is second part of exercise1 , where while loop will be used instad of for loop
#programe to find the ssum of any amount of numbers taken by users
def command():
    num=int(input("enter a number :",))
    return num
n=int(input("enter average of how many numbers do you want to calculate : ",))
sum=0
i=0
while(i<n):
    sum+=command()
    
    i+=1
average =sum/n
print("average  is :",average)
