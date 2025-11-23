#making a pyramid pattern 
n=int(input("enter the number of rows : ",))
for i in range (n):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(i):#writing i , instead of i+1 .because we need to write only one star in row 1 , not 2 
        print("$",end=" ")
    for l in range(i+1):
        print("$",end=" ")
    print()