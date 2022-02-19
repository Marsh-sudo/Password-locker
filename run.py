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

#create new credentials
def new_credentials(account,userName,password):
    '''
    function that creates new user credentials
    '''
    new_details = Credentials(account,userName,password)
    return new_details

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
        short_code = input().lower()

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