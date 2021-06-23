class Atm(object):
    def __init__(self,cardNumber,pinNumber):
       self.cardNumber=cardNumber
       self.pinNumber= pinNumber
    
    def CashWithdrawl(self):
        amount = int(input("Enter amount"))
        if(amount<10000):
            newAmount = 10000-amount
            print(f"You have withdrawn amount ${amount}.Your remaining balance is ${newAmount}")
        else:
            print("Insufficient balance")
    def BalanceEnquiry(self):
        print("Your balance is $10000")
    def CashDeposit(self):
        amount = int(input("Enter amount"))
        newAmount = 10000+amount
        print(f"You have deposited ${amount}.Your new balance is ${newAmount}")

def main():
    cardNumber=input("Enter your card number")
    pinNumber=input("Enter your pin number")
    
    newUser = Atm(cardNumber,pinNumber)
    print("Choose your activity: 1 balance enquiry 2 withdrawl 3 deposit")
    activity = int(input("Enter the activity number"))
    if(activity==1):
        newUser.BalanceEnquiry()
    elif(activity==2):
        newUser.CashWithdrawl()
    elif(activity==3):
        newUser.CashDeposit()
    else:
        print("Enter a valid option")

if __name__=="__main__":
    main()

    
