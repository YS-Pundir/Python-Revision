#opposite,increasing left handed  ,right angled triangle
n=int(input("enter the number of rows : ",))
for i in range(n):
    for j in range(i,n):#for  eg : when i is 0, the n 5= total star will be 5
        #when i is 1 , n is 5 = 5-1 is 4 , total star will be four ....and so on
        print("@",end=" ")
       
    print("")