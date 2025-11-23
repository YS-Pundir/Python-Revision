#making a Square pattern

n=int(input("entre the number of rows :  ",))
for i in range(n):
    for j in range(n):
        print("#",end=" ")
    print()#To change line after every row , as first loop is risponsible for the the rows in patterns
