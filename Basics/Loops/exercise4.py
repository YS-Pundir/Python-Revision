#program to add all the even numbers between numbers entered by user
a=int(input("eneter first number : ",))
b=int(input("enter second number :",))
sum=0
for i in range (a,b+1,2):
    sum+=i
print("sum of all even numbers between ",a,"and ",b,"is :",sum)