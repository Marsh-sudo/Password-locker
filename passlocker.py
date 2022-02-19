import pyperclip
class User:
    '''
    user class that generates new instances of the a user
    '''
    user_list = []

    def __init__(self,user_name,password):
        '''
        __init_method defines properties for our objects.
        '''
        self.user_name = user_name
        self.password = password

    def save_user(self):
            '''
            save_user method saves contact objects into user_list
            '''
            User.user_list.append(self)


class Credentials:
    '''
    credentials class that help in storing other user details.
    '''
    credential_list =[]

    def __init__(self,account,userName,passWord):
        '''
        __init__ method defines properties of our existing credentials.
        '''
        self.userName = userName
        self.passWord = passWord
        self.account = account

    def save_credentials(self):
            '''
            save_credentials method saves credentials object into the credentials_list
            '''

            Credentials.credential_list.append(self)


    @classmethod
    def find_by_username(cls,username):
            '''
            method that takes in a userName and returns the username info

            Args:
               username:username to search for
               Returns:
                 Username of person that matches the username
            '''

            for detail in cls.credential_list:
                if detail.userName == username:
                    return detail

    @classmethod
    def credentials_exist(cls,username):
        '''
        method to see if credentials exist in the list
        Args:
           username:username to test if it exist

        returns:
          boolean:true or false depending if contact exist 
        '''
        for details in cls.credential_list:
            if details.userName == username:
                return True

        return False   

    @classmethod
    def disply_credentials(cls):
        '''
        method that returns our list
        '''    
        return cls.credential_list

    
    @classmethod
    def copy_username(cls,account):
        username_found = Credentials.find_by_account(account)
        pyperclip.copy(username_found.userName)


    