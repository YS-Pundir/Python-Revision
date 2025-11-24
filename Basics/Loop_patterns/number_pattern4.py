#pyramid pattern with increment in single row
n=5
for i in range(n):
    p=1
    for j in range(i,n):
        print(" ",end=" ")
        
    for k in range(i+1):
        print(p,end=" ")
        p+=1
        
    
    for l in range(i):
        print(p,end=" ")
        p+=1
    print()