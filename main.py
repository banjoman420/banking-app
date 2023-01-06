# import json

# def loadFaves():
#   file = open("user_list.txt", "r")
#   data = json.load(file)
#   file.close()
#   return data

# #save contacts
# def saveFaves(fileToSave):
#   file = open("user_list.txt", "w")
#   json.dump(fileToSave, file)
#   file.close()

# class UserAccount:
#     def __init__(self, username, password, balance=0):
#         self.username = username
#         self.password = password
#         self.balance = balance

#     def signup(self):
#         user_list.append(self)

#     @classmethod
#     def login(cls, username, password):
#         for user in user_list:
#             if user.username == username and user.password == password:
#                 return user

#     def to_dict(self):
#         return {
#             "username": self.username,
#             "password": self.password,
#             "balance": self.balance
#         }
    
#     @classmethod
#     def from_dict(cls, data):
#         return cls(**data)

# class User:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def show_info(self):
#         print('\nPrinting all info:')
#         print('Name:', self.name)
#         print('Age:', self.age)
#         print('Gender:', self.gender)

# class Bank(User):
#     def __init__(self, name, age, gender):
#         super().__init__(name, age, gender)
#         self.bal = 0

#     def deposit(self, amount):
#         self.amount = amount
#         self.bal = self.amount + self.bal
#         print('You now have: $', self.bal)

#     def withdraw(self, amount):
#         self.amount = amount
#         if self.amount > self.bal:
#             print('Not enough money to withdraw')
#         else:
#             self.bal = self.bal - self.amount
#             print('Account balance now: $', self.bal)

#     def view_bal(self):
#         self.show_info()
#         print('Balance: $', self.bal)

# user_list = [UserAccount.from_dict(user) for user in loadFaves()]

# def main():
#     user_info = {}
#     name = input('What is your name? ')
#     age = input('What is your age? ')
#     gender = input('What is your gender? ')

#     user_info['name'] = name
#     user_info['age'] = age
#     user_info['gender'] = gender

#     person = Bank(**user_info)

#     main_loop = True
#     while main_loop:
#         print(
#             '''
#             1. Add money
#             2. Withdraw money
#             3. View balance
#             '''
#         )

#         numpick = input('What option would you like (pick the number)? ')

#         if numpick == '1':
#             amount = int(input('How much money would you like to deposit? '))
#             person.deposit(amount)
#         elif numpick == '2':
#             amount = int(input('How much money would you like to withdraw? '))
#             person.withdraw(amount)
#         elif numpick == '3':
#             person.view_bal()

# main()


# def user_account():
#     loop_creds = True
#     while loop_creds:
#         print('''
#         1. sign up
#         2. login 
#         ''')

#         accauntPick = input("input the number of the option you want (1 or 2)")

#         # sign up
#         if accauntPick == "1":
#             # ask user for username and password
#             username, password = get_info()
#             user = UserAccount(username, password)
#             user.signup()
#             saveFaves([user.to_dict() for user in user_list])
#             return user
#             loop_creds = False
#         # login
#         elif accauntPick == "2":
#             # get username and password from user
#             username, password = get_info()
#             user = UserAccount.login(username, password)
#             print('login complete')
#             return user
#             loop_creds = False
#         else:
#             print('enter a correct number (1 or 2)')

# def get_info():
#     username = input('what is your username')
#     password = input('what is your password')
#     return username, password

# user_account()

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
    username = input('what is your username')
    password = input('what is your password')
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

