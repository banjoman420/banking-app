import json

class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_info(self):
        print('\nPrinting all info:')
        print('Name:', self.name)
        print('Age:', self.age)
        print('Gender:', self.gender)

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.bal = 0

    def deposit(self, amount):
        self.amount = amount
        self.bal = self.amount + self.bal
        print('You now have: $', self.bal)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.bal:
            print('Not enough money to withdraw')
        else:
            self.bal = self.bal - self.amount
            print('Account balance now: $', self.bal)

    def view_bal(self):
        self.show_info()
        print('Balance: $', self.bal)

        

def main():
    user_info = {}
    name = input('What is your name? ')
    age = input('What is your age? ')
    gender = input('What is your gender? ')

    user_info['name'] = name
    user_info['age'] = age
    user_info['gender'] = gender

    person = Bank(**user_info)

    main_loop = True
    while main_loop:
        print(
            '''
            1. Add money
            2. Withdraw money
            3. View balance
            '''
        )

        numpick = input('What option would you like (pick the number)? ')

        if numpick == '1':
            amount = int(input('How much money would you like to deposit? '))
            person.deposit(amount)
        elif numpick == '2':
            amount = int(input('How much money would you like to withdraw? '))
            person.withdraw(amount)
        elif numpick == '3':
            person.view_bal()

main()