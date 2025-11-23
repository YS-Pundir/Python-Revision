#opposite number pattern , decriment in numbers by row
n=int(input("enteer the number of rows : "))
p=n
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
    p-=1
    print()