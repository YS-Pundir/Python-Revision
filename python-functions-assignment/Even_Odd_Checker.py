n=int(input("Enter the number of your wish : ",))

def checker(n):
    if n%2==0:
        return "The number is even"
    else:
        return "Number is odd"

print(checker(n))