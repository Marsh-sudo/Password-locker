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

    def __init__(self,userName,passWord):
        '''
        __init__ method defines properties of our existing credentials.
        '''
        self.userName = userName
        self.passWord = passWord

    def save_credentials(self):
            '''
            save_credentials method saves credentials object into the credentials_list
            '''

            Credentials.credential_list.append(self)
    