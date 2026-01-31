Balance=int(input("Balance : ",))
Withdrawal=int(input("withdrawal : ",))
varified=bool(input("Varified (True/False): "))

if varified == "True" and Withdrawal<=Balance:
    print("Withdrawal Succeessfull ")
else:
    print("Withdrawal denied")