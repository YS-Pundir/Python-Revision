#right handed decreasing right handed triangle,
n =int(input("enter the number of rows in the pattern : ",))
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(i,n):
        print("&",end=" ")
    print()

