#programe to check if widthdrwal  the amount form bank  account is possible or not
c_b=50000
wb=int(input("Enter the withdrawl amount : ",))
if wb>c_b:
    print("INsufficcient balance . You can withdrawl up to ",c_b)
else :
    print("please Collect your Cash . your current balance is ",c_b-wb,"\n Thank you for visiting our bank . ")