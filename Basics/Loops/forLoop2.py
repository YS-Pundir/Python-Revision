#program to find the sum between two numbers
a=int(input("enter first number:",))
b=int(input("enter second number:",))

sum=0
for i in range (a,b+1):
    sum=sum+i

print("the sum of numbers between ",a,"and ",b,"is : ",sum)