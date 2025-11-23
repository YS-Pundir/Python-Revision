#just printing 1 in left sided triangle
n=int(input("enter the number of rows : ",))
for i in range (n):
    for j in range(i+1):
        print("1",end=" ")
    print()