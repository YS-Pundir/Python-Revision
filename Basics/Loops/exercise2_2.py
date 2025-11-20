#Finding the product of first n numbers using while loop
n=int(input("enter a number :",))
product=1
i=1
while(i<=n):
    product*=i
print(" the product of first",n,"numbers is : ",product)