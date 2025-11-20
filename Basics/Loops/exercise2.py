#Finding the product of first n numbers using for loop
n=int(input("enter a number :",))
product=1
for i in range(1,n+1):
    product*=i
print(" the product of first",n,"numbers is : ",product)