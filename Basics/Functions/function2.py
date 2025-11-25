#function to swap two numbers
a=int(input("enter the first number :",))
b=int(input("enter the second number :",))

#function to swwap the value of both numbers
def swap(a,b):
    temp=a
    a=b
    b=temp


    print("the value of a now is :",a)
    print(f"the value of b now is {b} ")
swap(a,b)
