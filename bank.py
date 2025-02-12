import csv


class Bank:
    
    def __init__(self):
        self.customers = []
        self.load_accounts()
        self.account_num = len(self.customers) if self.customers else 0
        
    def create(self, name, contact, initial_deposit):
        self.customers.append({
            'account_num': self.account_num, 
            'name': name, 
            'contact': contact, 
            'balance': initial_deposit, 
            'initial_deposit': initial_deposit, 
            'transaction_logs': []
        })
        
        for customer in self.customers:
            if customer['account_num'] == self.account_num:
                customer['transaction_logs'].append({
                    'amount': initial_deposit, 
                    'transaction': 'initial deposit', 
                    'current_balance': customer['balance']
                })
                
        self.account_num += 1
        print(f"Account created successfully with account num : {self.customers[self.customers.__len__() - 1]['account_num']}")
        self.save_accounts()
    
    def deposit(self, account_num, amount):
        for customer in self.customers:
            if customer['account_num'] == account_num:
                customer['balance'] += amount
                customer['transaction_logs'].append({
                    'amount': amount, 
                    'transaction': 'credit', 
                    'current_balance': customer['balance']
                })
                print("Deposit successful")
                self.save_accounts()
                return
        print('Account number not found')
        
    def withdraw(self, account_num, amount):
        for customer in self.customers:
            if customer['account_num'] == account_num:
                if customer['balance'] >= amount:
                    customer['balance'] -= amount
                    customer['transaction_logs'].append({
                        'amount': amount, 
                        'transaction': 'debit', 
                        'current_balance': customer['balance']
                    })
                    print('Withdraw successful')
                    self.save_accounts()
                    return
                else:
                    print('Not enough balance')
                    return
        print('Account number not found')
        
    def account_statement(self, account_num):
        for customer in self.customers:
            if customer['account_num'] == account_num:
                print(f"Transaction logs for account number {account_num} \n {customer['transaction_logs']}")
                return
        print('Account number not found')
    
    def save_accounts(self):
        with open('accounts.csv', 'w', newline='') as f:
            fields = [
                'account_num', 'name', 'contact',
                'initial_deposit', 'balance', 'transaction_logs'
            ]
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            for customer in self.customers:
                writer.writerow({
                    'account_num': customer['account_num'],
                    'name': customer['name'],
                    'contact': customer['contact'],
                    'initial_deposit': customer['initial_deposit'],
                    'balance': customer['balance'],
                    'transaction_logs': str(customer['transaction_logs'])
                })

    def load_accounts(self):
        try:
            with open('accounts.csv', 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.customers.append({
                        'account_num': int(row['account_num']),
                        'name': row['name'],
                        'contact': row['contact'],
                        'initial_deposit': int(row['initial_deposit']),
                        'balance': int(row['balance']),
                        'transaction_logs': eval(row['transaction_logs'])
                    })
        except Exception as e:
            print(f"Error loading accounts: {e}")


bank = Bank()

while(True):
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
        break
    else:
        print('Invalid Choice') 
