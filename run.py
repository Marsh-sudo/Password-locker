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

def del_user(user):
    '''
    function to delete a user
    '''
    user.delete_user()