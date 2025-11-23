#adding right angled triangle
n=int(input("enter the number of rows  : ",))
for i in range(n):
    for j in range(i+1):#"i+1", because the star in column is one more everytime then the no of row it is in 
        print("$",end=" ")
    print()
