#function to find the factorial of any number
n=int(input("enter any number : ",))

def factorial(n):
    result=1
    for i in range(1,n+1):
        
        result*=i
    return result
print("the factorial  of the number is ",factorial(n))
    
    
    