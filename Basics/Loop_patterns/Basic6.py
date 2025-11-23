#pattern for inverted pyramid
n=int(input("enter the number of rows :",))
for i in range(n):
    for j in range (i+1):
        print(" ",end=" ")
    for k in range(i+1,n):#eg  , f=printing from 1 to 4
        print("#",end=" ")
    for l in range(i,n):
        print("#",end=" ")
    print()