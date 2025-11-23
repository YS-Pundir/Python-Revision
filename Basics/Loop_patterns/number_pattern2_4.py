#left sided pattern , with numbers being incremented in single row .
n=5
for i in range(n):
    p=1
    for i in range(i,n):
        print(p,end=" ")
        p+=1
    print()
    