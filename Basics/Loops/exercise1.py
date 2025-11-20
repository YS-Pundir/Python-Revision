#program to find average of n random numbers entered by user 
def command():
    num=int(input("enter a number :",))
    return num
n=int(input("enter average  of how many numbers do you want:"))
sum=0
for i in range(n):
    sum+=command()
average=sum/n
print("average is :",average)
