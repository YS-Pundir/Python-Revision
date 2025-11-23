#Staringht pyramid , with number being incrimented by one 
n=int(input("enter the number of rows for it : ",))
for i in range (n):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(i):
        print(i+1,end=" ")
    for l in range(i+1):
        print(i+1,end=" ")
    print()