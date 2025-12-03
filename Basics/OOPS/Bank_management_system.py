class BankAccount():
    print("Hallo ,Herzlich willkommen bie Sparkasse .\nwir wunchen euch einer shones Tag")
    def __init__(self,Accont_holder,AccountNumber,Balance):
        self.Accont_holder=Accont_holder
        self.AccountNumber=AccountNumber
        self.Balance=Balance
    
    def deposite(self):
        amount=int(input("enter the amount that need to be deposite :",))
        self.Balance+=amount
        print(f"The updated Bank Balance is : {self.Balance}")

    def withdrawal(self):
        amount=int(input("enter the amount that need to be withdraw : ",))
        if amount<self.Balance:
            print("The Withdrawal amount is laarger than the Account Balance .\nPlease enter smaller amount to be withdrawed")

        else:
            print(f"The amount of {amount} has been withdrwal from your bank account ")
            self.Balance-=amount
            print(f"The updated amount of the Bank Account is {self.Balance} .\nThanks for visiting  us :)")

class Manage(BankAccount):
    def __init__(self,Accont_holder,AccountNumber,Balance,Password):
        super().__init__(Accont_holder,AccountNumber,Balance)
        self.Password=Password
        
    def New_Holder(self):
        Name=input("please enter the name of new Account Holder : ",)
        self.Accont_holder=Name
        print(f"The name of Account holder is updated .\n the updated name of Account Holder is {self.Accont_holder}")

    def ShowBalance(self):
        print(f"the Account has {self.Balance}euros ")

    def key(self):
        Key=int(input("enter the password of the acount : ",))
        if(Key==self.Password):
            print("A:Withdrwal\nB:Deposite\nC:Change User Name \nD:Check Balance")
            service=input("please choose one option from the given services -",)
            
            if(service!="A"and service!="B" and service !="C" and service!="D"):
                print("<>----Invalid input----<>")
            elif(service=="A"):
                user.withdrawal()
            elif(service=="B"):
                user.deposite()
            elif(service=="C"):
                user.New_Holder()
            elif(service=="D"):
                user.ShowBalance()
        else:
            print("Wrong Password")


user=Manage("Yuvraj Singh",12345,360000,5200)
user.key()









        
