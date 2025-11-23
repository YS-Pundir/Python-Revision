#making a right handed increasing triangle:
n=int(input("enter the number of rows : ",))
for i in range(n):
    for j in range(i,n):#if n=5 , at first step , print space from 0 to 4 
        print(" ",end=" ")
    for k in range(i+1):#print ₹ on i+1,it means 5
        print("₹",end=" ")
    print(' ')