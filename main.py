'''
basic banking operation system
'''


class Bank:
    bankname="Pubali Bank Limited"
    branch="7,Adampur,Sylhet"

    #create account
    def __init__(self,username,pin,address):
        self.username=username
        self.pin=pin
        self.address=address
        self.balance=0.0 # setting account balance to 0.0
        print(f'Hello {self.username}, Your account created successfully')

    #depoist
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f'{amount} deposited successfully.Your new balance is {self.balance}')

    #withdraw
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount
            print(f'{amount} withdrawn successfully.Your new balance is {self.balance}')
        else:
            print('Insufficent Fund...')

    #statement
    def statement(self):
        print(f'Your account balance is {self.balance}')


print(f'Welcome to {Bank.bankname}  {Bank.branch}')
#collecting user data for account creation
username=input('Enter Your name : ')
pin=input('Enter PIN card number : ')
address=input('Enter Your address : ')

b=Bank(username,pin,address) # object creation based on user provided data

while True:
    print('Please Select any Option : ')
    print('1.Deposit\n2.Withdraw\n3.Ministatement\n4.Stop')
    option=int(input(''))

    if option==1:
        amount=float(input('Enter Deposited amount : '))
        b.deposit(amount)

    elif option==2:
        amount=float(input('Enter Withdraw amount : '))
        b.withdraw(amount)

    elif option==3:
        b.statement()

    elif option==4:
        print(f'Thanks for using {Bank.bankname}')
        break
    else:
        print('Invalid Option please select a  valid option')
