#!/usr/bin/env python3.6
from passlocker import User,Credentials

def create_contact(account,username,password):
    '''
    Function to create a new account details
    '''

    new_account = User(account,username,password)
    return new_account