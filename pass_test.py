import unittest
from passlocker import User

class TestPass(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unitest.TestCase:TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        set up method to run before each test cases.
        '''
        self.new_user = User("Kelvin","kel0123") #create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"Kelvin")
        self.assertEqual(self.new_user.password,"kel0123")
    
    
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved in
        the user list
        '''
        self.new_user.save_contact() #saving the user details
        self.assertEqual(len(User.user_list),1)