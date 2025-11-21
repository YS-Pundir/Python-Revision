#program to add all the even numbers between numbers entered by user
a=int(input("eneter first number : ",))
b=int(input("enter second number :",))
sum=0
for i in range (a,b+1):
    if(i%2==0):
        sum+=i
    else:
        continue
print("the sum of all even numbers betwee ",a,"and ",b,"is :",sum)
