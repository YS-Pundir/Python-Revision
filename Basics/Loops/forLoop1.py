# this code is to find the sum of first five numbers using a loop
n=int(input("Enter a number:"),)
sum=0
if(n<0):
    print("pleasee enter a positive number")
    
else:
    for i in range(n):
        sum+=i
    print(sum)


