#diamond shape for first increment and then decrement
n=5
p=1
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(i+1):
        print(p,end=" ")
    for l in range(i):
        print(p,end=" ")
    p+=1
    print()
p=5
for i in range(n):
    for j in range(i+1):
        print(' ',end=" ")
    for k in range(i+1,n):
        print(p,end=" ")
    for l in range(i,n):
        print(p,end=" ")
    p-=1
    print()
