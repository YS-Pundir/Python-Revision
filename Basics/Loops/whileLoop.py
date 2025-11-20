#program to find sum of number until  -999 is entered
num=int(input("enter a number : ",))
sum=0
while(num!=-999):
    sum+=num
    num=int(input("enter a number : ",))

print("the sum is :",sum)

