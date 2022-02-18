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
    