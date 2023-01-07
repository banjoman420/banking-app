#basic banking system using OOP
import json

def loadUsers():
  file = open("user_list.txt", "r")
  data = json.load(file)
  file.close()
  return data

#save users
def saveUsers(fileToSave):
  file = open("user_list.txt", "w")
  json.dump(fileToSave, file)
  file.close()

class UserAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance

    def signup(self):
        for user in user_list:
            if user.username == self.username:
                print("Username already in use. Please choose a different username.")
                return None
        user_list.append(self)
        return self

    @classmethod
    def login(cls, username, password):
        for user in user_list:
            if user.username == username and user.password == password:
                return user
        return None

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "balance": self.balance
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposit of ${amount} successful. New balance: ${self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Not enough money to withdraw')
        else:
            self.balance -= amount
            print(f'Withdrawal of ${amount} successful. New balance: ${self.balance}')

user_list = [UserAccount.from_dict(user) for user in loadUsers()]

def user_account():
    loop_creds = True
    while loop_creds:
        print('''
        1. sign up
        2. login 
        ''')

        accauntPick = input("input the number of the option you want (1 or 2)")

        # sign up
        if accauntPick == "1":
            username, password = get_info()
            user = UserAccount(username, password)
            user = user.signup()
            if user is None:
                print('username is already in use')
                continue
            saveUsers([user.to_dict() for user in user_list])
            return user
            loop_creds = False
        # login
        elif accauntPick == "2":
            # get username and password from user
            username, password = get_info()
            user = UserAccount.login(username, password)
            if user is None:
                print("Invalid username or password. Please try again.")
            else:
                print('login complete')
                return user
                loop_creds = False
        else:
            print('enter a correct number (1 or 2)')

def get_info():
    while True:
        username = input('what is your username')
        if not username:
            print("Username cannot be empty. Please enter a valid username.")
            continue
        password = input('what is your password')
        if not password:
            print("Password cannot be empty. Please enter a valid password.")
            continue
        return username, password

class Bank:
    def __init__(self, user):
        self.user = user

    def main_menu(self):
        main_loop = True
        while main_loop:
            print(
                '''
                1. Deposit money
                2. Withdraw money
                3. View balance
                4. Exit
                '''
            )

            numpick = input('What option would you like (pick the number)? ')

            if numpick == '1':
                amount = int(input('How much money would you like to deposit? '))
                self.user.deposit(amount)
            elif numpick == '2':
                amount = int(input('How much money would you like to withdraw? '))
                self.user.withdraw(amount)
            elif numpick == '3':
                print(f'Current balance: ${self.user.balance}')
            elif numpick == '4':
                saveUsers([user.to_dict() for user in user_list])
                main_loop = False
            else:
                print('Invalid option. Please try again.')

def main():
    user = user_account()
    bank = Bank(user)
    bank.main_menu()
main()