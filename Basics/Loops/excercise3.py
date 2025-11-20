#finding product of any numbers entered by user 
def command():
    return int(input("enter a number :",))
product=1
n=int(input("how many numbers yiu want to enter :",))
for i in range(n):
    product*=command()
print("the product of all the numbers that you entered is :",product)