class BankAccount:
    text = '\n SELECT ACTION FROM THE LIST:' \
           '\n Enter 1: Deposit money to your account' \
           '\n Enter 2: Withdraw money from your account' \
           '\n Enter 3: Close an account '

    def __init__(self):
        self.name = input(' Please, enter your name: ').capitalize()
        print(' Hello, {name}!'.format(name=self.name))
        question = input('\n OPEN AN ACCOUNT? (y/n): ').lower()
        if question == 'yes' or question == 'y':
            self.money = 0
            self.get_action(input(BankAccount.text))
        else:
            return

    def get_action(self, action):
        action = int(action)
        if action == 1:
            self.add_money(input('\n Enter amount of cash: '))
        elif action == 2:
            self.withdraw_money(input(' Enter amount of cash: '))
        elif action == 3:
            self.close_account()
        else:
            return

    def add_money(self, amount):
        amount = int(amount)
        for i in range(3):
            if amount == 0:
                amount = int(input(' Please, enter a value greater than zero,'
                                   '\n try again ({tries} tries remind). '.format(tries=(3 - i))))
            else:
                self.money += int(amount)
                print(' The account was credited successfully on {amount}'.format(amount=amount) + ' UAH')
                print(' Current account balance: ' + str(self.money) + ' UAH')
                break
        self.get_action(input(BankAccount.text))

    def withdraw_money(self, amount):
        amount = int(amount)
        for i in range(3):
            if amount == 0 or amount > self.money:
                amount = int(input(' Insufficient funds in the account,'
                                   '\n try again ({tries} tries remind). '.format(tries=(3 - i))))
            else:
                self.money -= amount
                print(' Current account balance: ' + str(self.money) + ' UAH')
                break
        self.get_action(input(BankAccount.text))

    def close_account(self):
        return print(' Goodbye, {name}!'.format(name=self.name))


new_account = BankAccount()

