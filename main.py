class BankAccount:
    def __init__(self):
        self.balance = 20000
        print('WELCOME TO SOMA TRUST BANK LTD')
        print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')

    def PinCode(self):
        while True:
            pin = input('Enter your pin: ')
            if len(pin) == 4:
                try:
                    pin == int(pin)
                    return pin
                    break
                except:
                    return ('Invalid pin code')
            else:
                print('Your pin is incorrect')

    def Deposit(self):
        while True:
            Amount = input('Enter amount you want to deposit: ')
            try:
                Amount = int(Amount)
                if Amount > 0:
                    NewBalance = self.balance + Amount
                    return f'\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\nAmount Deposited: USH.{Amount}\nAccount Balance: USH.{NewBalance}'
                else:
                    print('Please enter correct amount')
            except:
                print('Deposit amount must be in integers')

    def Withdraw(self):
        while True:
            Amount = input('Enter withdraw amount: ')
            try:
                Amount = int(Amount)
                if Amount <= self.balance:
                    NewBalance = self.balance - Amount
                    return f'\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\nAmount Withdrawn: USH.{Amount}\nAccount Balance: USH.{NewBalance}'
                else:
                    print('Insuficient balance')
            except:
                    print('Withdraw amount must be in integers')

    def CheckBalance(self):
        return f'You account balance is USH.{self.balance}'

    def TransactionId(self):
        import random
        return f'Transaction ID: {random.randint(100000000000, 1000000000000)}\nTHANK YOU!\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°'

    def date(self):
        import datetime
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        print(f'DATE: {day}/{month}/{year}')
        hour = now.hour
        minute = now.minute
        second = now.second

        print(f'TIME: {hour} : {minute} : {second}')

    def Quiting(self):
        print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
        print(f'THANK YOU FOR CHOOSING SOMA TRUST BANK, PLEASE COME AGAIN')

s = BankAccount()
print(s.PinCode())
while True:
    print('\nOPERATIONS')
    print('1.Deposit')
    print('2.Withdraw')
    print('3.Check Balance')
    print('4.Quit\n')
    Operation = input('Please choose operation(1, 2, 3, or 4): \n')

    try:
        Operation = int(Operation)
        if Operation in (1, 2, 3, 4):
            if Operation in (1, 2, 3, 4):
                if Operation == 1:
                    print(s.Deposit())
                    print(s.date())
                    print(s.TransactionId())

                elif Operation == 2:
                    print(s.Withdraw())
                    print(s.date())
                    print(s.TransactionId())

                elif Operation == 3:
                    print(s.CheckBalance())
                    print(s.date())
                    print(s.TransactionId())

                elif Operation == 4:
                    print(s.Quiting())
                    break
        else:
            print(f'Operation {Operation} is not available')

    except:
        print('Please choose option in form of 1,2,3 or 4')

52

