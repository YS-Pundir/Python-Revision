#program to find sum of all odd numbers between numbers entered by user
a=int(input("enter first number :",))
b=int(input("enter the second number :",))
sum=0
for i in range(a,b+1):
    if(i%2==0):
        continue
    else:
        sum+=i
print("sum of all odd numbers between ",a,"and ",b,"is :",sum)