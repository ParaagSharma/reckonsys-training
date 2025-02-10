class Bank:
    
    def __init__(self):
        self.account_num = 0
        self.customers = []
        
    def create(self, name, contact, initial_deposit):
        self.customers.append({'account_num': self.account_num, 'name': name, 'contact': contact, 'initial_deposit': initial_deposit, 'transaction_logs': []})
        self.account_num += 1
        print(f"Account created successfully with account num : {self.customers[self.customers.__len__() - 1]['account_num']}")
        return
    
    def deposit(self, account_num, amount):
        for customer in self.customers:
            if customer['account_num'] == account_num:
                customer['initial_deposit'] += amount
                customer['transaction_logs'].append({'amount': amount, 'transaction': 'credit'})
                print("Deposit successful")
                return
        print('Account number not found')
        
    def withdraw(self, account_num, amount):
        for customer in self.customers:
            if customer['account_num'] == account_num:
                customer['initial_deposit'] -= amount
                customer['transaction_logs'].append({'amount': amount, 'transaction': 'debit'})
                print('Withdraw successful')
                return
        print('Account number not found')
        
    def account_statement(self, account_num):
        for customer in self.customers:
            if customer['account_num'] == account_num:
                print(f"Transaction logs for account number {account_num} \n {customer['transaction_logs']}")
                return
        print('Account number not found')
    

bank = Bank()
flag = True
while(flag):
    print('Banking Operations System')
    print('1 - Account Creation')
    print('2 - Deposit Money')
    print('3 - Withdraw Money')
    print('4 - Account Statement')
    print('5 - Exit')
    choice = int(input('Enter choice: '))

    if choice == 1:
        name = input("Enter Name: ")
        contact = input("Enter Contact: ")
        initial_amount = int(input("Enter Initial Amount: "))
        bank.create(name=name, 
                    contact=contact, 
                    initial_deposit=initial_amount
            )
    elif choice == 2: 
        account_num = int(input('Enter your account number: '))
        amount = int(input('Enter the amount: '))
        bank.deposit(account_num=account_num,
                        amount=amount
            )
    elif choice == 3:
        account_num = int(input('Enter your account number: '))
        amount = int(input('Enter the amount: '))
        bank.withdraw(account_num=account_num,
                        amount=amount
            )
    elif choice == 4:
        account_num = int(input('Enter your account number: '))
        bank.account_statement(account_num=account_num)
    elif choice == 5:
        flag = False
    else:
        print('Invalid Choice') 
