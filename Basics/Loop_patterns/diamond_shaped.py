#printing the diamond shaped number pattern 
n=5
p=1
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for l in range(i):
        print(p,end=" ")
    for k in range(i+1):
        print(p,end=" ")
    p+=1
    print()
for i in range(n):
    for j in range(i+1):#so that row of 6 would be less than row of 5
        print(" ",end=" ")
    for k in range(i,n):
        print(p,end=" ")
    for l in range(i+1,n):
        print(p,end=" ")
    p+=1
    print()
        




