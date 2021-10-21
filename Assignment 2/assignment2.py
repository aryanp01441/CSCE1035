'''
FileName = assignment2.py
Author = Aryan Patel
Created on: 9/17/21
Description: simple Python 3 banking application
'''

# function for password encryption
def password (user_password):
    # variable use to encrypt the password
    encrypted_password = ' '

    i = 0

    while i < len(user_password):
        # temporarly variable used to store the ASCII value of the password
        temp = ord(user_password[i])
        if 65 <= temp <= 90:
            if temp == 88:
                temp = 65
            elif temp == 89:
                temp = 66
            elif temp == 90:
                temp = 67
            else:
                temp += 3
            encrypted_password += chr(temp)
        elif 97 <= temp <= 122:
            if temp == 120:
                temp = 97
            elif temp == 121:
                temp = 98
            elif temp == 122:
                temp = 99
            else:
                temp += 3
            encrypted_password += chr(temp)
        elif 48 <= temp <= 57:
            if temp == 55:
                temp = 48
            elif temp == 56:
                temp = 49
            elif temp == 57:
                temp = 50
            else:
                temp += 3
            encrypted_password += chr(temp)
        else:
            temp = temp
            encrypted_password += chr(temp)
        i += 1
    return encrypted_password

# deposit function
def deposit (deposit_amount):
    temp = user_information["User balance"]     # temp variable to store user current balance
    bank_balance = temp + deposit_amount        # Adding deposited amount with current balance
    user_information["User balance"] += deposit_amount  # Updating current balance
    print('New balance: {:.2f}'.format(bank_balance))

# withdraw function
def withdraw(withdraw_amount):
    temp = user_information["User balance"]     # temp variable to store user current balance
    bank_balance = temp - withdraw_amount       # Minusing withdrawed amount with current balance
    user_information["User balance"] -= withdraw_amount # Updating current balance
    print('New balance: {:.2f}'.format(bank_balance) )

# displaying personal information
print('+--------------------------------------------+')
print('|       Computer Science and Engineering     |')
print('|     CSCE 1035 - Computer Programming I     |')
print('|   Aryan Patel asp0144 asp0144@my.unt.edu   |')
print('+--------------------------------------------+')

# declaring dictionary
user_information = {"User ID": '', "Encrypted password": '', "User balance": 0}

# Asking and storing user ID
user_id = input('Enter new used ID: ')
i = 0
while i < len(user_id):
    user_information["User ID"] += user_id[i]
    i += 1

# Asking and storeing user password
user_password = input('Enter password: ')
temp_password = password(user_password)
i = 0
while i < len(user_password):
    user_information["Encrypted password"] += temp_password[i]
    i += 1

# Asking and storing user current balance
user_initial_balance = float(input('Enter initial balance: $'))
user_information["User balance"] = user_information["User balance"] + user_initial_balance

user_choice = 0
user_login = False  # User not logged in

while user_choice != 6:
    # Printing the menu
    print('******************* M E N U *****************+')
    print('| Select a service:                          |')
    print('| 1. Login to Account                        |')
    print('| 2. Deposit to Account                      |')
    print('| 3. Withdraw from Account                   |')
    print('| 4. Print Balance                           |')
    print('| 5. Change Password                         |')
    print('| 6. Exit/Logout                             |')
    print('*********************************************+')
    user_choice = int(input('Enter choice> '))
    # if user not logged in and user choice is between 1 and 5
    if user_login == False and 1 <= user_choice <= 5:
        if user_login != True and user_choice != 1:     # if user not logged in and try to select a service
            print('Unable to perform transaction - user not logged in')
            user_login = False
        elif user_login != True and user_choice == 1:
            login_id = input('Enter user ID : ')
            login_password = input('Enter password : ')
            if login_id != user_id or login_password != user_password:
                print('Unable to login - invalid user ID or password')
            if login_id == user_id and login_password == user_password:
                print('User', login_id, 'logged in to account')
                user_login = True   # updating login status
    elif user_login == True and 1 <= user_choice <= 5:
        if user_choice == 1:
            print('User already logged in')
        elif user_choice == 2:
            deposit_amount = float(input('Enter deposit amount: ')) # taking in amount of money user want to deposit
            deposit(deposit_amount)     # calling deposit function
        elif user_choice == 3:
            withdraw_amount = float(input('Enter withdraw amount: '))   # taking in amount of money user wants to withdraw
            if withdraw_amount > user_information["User balance"]:
                print('Transaction denied - insufficient funds')
            else:
                withdraw(withdraw_amount)
        elif user_choice == 4:
            print(user_id + ' balance: $' + str(user_information["User balance"]))
        elif user_choice == 5:
            new_password = input('Enter new password: ')    # taking in new password
            temp1_password = password(new_password)         # temp variable to hold encrypted password
            user_information.update({"Encrypted password" : temp1_password})    # updating password in dictionary
    elif user_choice == 9:
        print(user_information ["User ID"], end=' ')
        print(user_information ["Encrypted password"], end=' ')
        print(user_information ["User balance"])
    elif user_choice == 6:
        print('User', user_id, 'logged out of account')
        print('Thank you for holding your account with us')
        break
    else:
        print('Invalid selection - please try again')