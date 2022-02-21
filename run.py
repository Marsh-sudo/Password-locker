#!/usr/bin/env python3.6
from passlocker import User,Credentials

def create_users(account,username,password):
    '''
    Function to create a new account details
    '''

    new_user = User(account,username,password)
    return new_user

def save_users(user):
    '''
    function to save user
    '''
    user.save_user()

def login_user(username,password):
    '''
    function to show if user exist
    '''
    user = User.exist_user(password,username)
    return user


#create new credentials
def new_credentials(account,Username,password):
    '''
    function that creates new user credentials
    '''
    new_details = Credentials(account,Username,password)
    return new_details

def save_details(credentials):
    '''
    function that save our new credentials
    '''
    credentials.save_details()

def del_user(credentials):
    '''
    function to delete a user
    '''
    credentials.delete_user()

  #finding a user
def find_user(username):
    '''
    function that finds a user by account and returns the contact
    '''
    return Credentials.find_by_username(username)

#user existence
def check_existing_users(username):
    '''
    function that check if a user exist with that username and returns a boolean
    '''
    return Credentials.user_exist(username)

    #display all credentials

def display_credentials():
    '''
    function that returns all the saved credentials
    '''
    return Credentials.disply_credentials()



def main():
    print("Hello.Welcome to your Credentials Centre.What is your name?")
    name = input()

    print(f"Hello {name}.What would you like to do?")
    print('\n')

    while True:
        print("Use the short codes : To create account with Us!-cc, Already have an account?-ac")
        short_code = input()

        if short_code == 'cc':
            print("New User")
            print("-"*10)

            print("Usernmae...")
            username = input()
            password = ""

            while True:
                print("Use the codes to create password: To create password-tc,Randomly generate password-rp")
                user_choice = input()
                if user_choice == 'tc':
                    password = input()
                    
                    break

                else:
                    print('Must have password')
            
            save_users(create_users(username,password))
            print('Heyy {username},Thanks for creating an account ;) Your password is:{password} ')

        elif short_code == 'ac':
            print('Welcome:)..Enter your username and password to login in:')
            username = input()
            password = input()
            
            exist = login_user(username,password)
            if login_user == exist:
                print(f'Hello {username} Happy to see you back!')

            while True:
                print('Use this short codes: Add new Credentials-CC,display Credential-DA,Search Credentials-SC,Exit the App-EX')
                short_code == input()

                if short_code == 'CC':
                    print('New Credentials')

                    print('Account...')
                    acc_name = input()

                    print('Username...')
                    user_name = input()

                    while True:
                        print('Use codes: To create new password-tp,')
                        pass_choice = input()
                        if pass_choice == 'tp':
                            passwordd = input()

                            break
                        else:
                            print('Password Needed')

                    save_details(new_credentials(username,password))
                    print('\n')
                    print(f'Account:{acc_name}, Username: {user_name}, Password: {passwordd} have been added to list')

                elif short_code == 'DA':
                    if display_credentials():
                        print('Here are your credentials')
                        print('\n')

                        for detail in display_credentials():
                            print(f'{detail.account} {detail.Username}....{detail.password}')
                        
                        print('\n')
                    
                    else:
                        print('\n')
                        print('Oops!!! seems you dont have any credentials')

            
                elif short_code == 'SC':
                    print('Enter username you want to search;')

                    search_detail = input()
                    if check_existing_users(search_detail):
                        search_user = find_user(search_detail)
                        print(f'Account....{search_user.account}')
                        print(f'Username....{search_user.Username}')
                        print(f'Password....{search_user.password}')

                    else :
                        print("Ooops!! Invalid Credentials")

                elif short_code == 'EX':
                    print('Thank you for using Me....Adios!!')

                    break
                else:
                    print("I really didn't understand your Command!!! Please use the short codes!")


if __name__ == '__main__':
    main()
                        





                