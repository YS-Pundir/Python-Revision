class BankAccount():
    def __init__(self,Accont_holder,AccountNumber,Balance):
        self.Accont_holder=Accont_holder
        self.AccountNumber=AccountNumber
        self.Balance=Balance
    
    def deposite(self):
        amount=input("enter the amount that need to be deposite :",)
        self.Balance+=amount
        print(f"The updated Bank Balance is : {self.Balance}")

    def withdrawal(self):
        amount=input("enter the amount that need to be withdraw : ",)
        if amount<self.Balance:
            print("The Withdrawal amount is laarger than the Account Balance .\nPlease enter smaller amount to be withdrawed")

        else:
            print(f"The amount of {amount} has been withdrwal from your bank account ")
            self.Balance-=amount
            print(f"The updated amount of the Bank Account is {self.Balance} .\nThanks for visiting  us :)")
            

        
