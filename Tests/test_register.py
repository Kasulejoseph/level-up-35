import unittest
from .register import signUp

class testRegister(unittest.TestCase):


    def setUp(self):
        self.signup = signUp()
        self.signup.firstName("name","dsjh 5fdg")
        self.signup.lastName("name","joseph")
        self.signup.email("mail","kasule@gmail.com")

    def test_creation(self):
        '''
        Test for pressence of signup class
        '''
        self.assertIsInstance(self.signup,signUp)
    
    def test_firstName_exists(self):
        '''
        Test if first name exists
        '''
        self.signup.firstName("name","kasule")
        self.assertEqual(len(self.signup.fname),1)

    def test_lastName_exists(self):
        self.signup.lastName("name","joseph")
        self.assertEqual(len(self.signup.lname),1)

    def test_email_exists(self):
        self.signup.email("mail","kasule@gmail.com")
        self.assertEqual(len(self.signup.emails),1)

    def test_is_string(self):
        '''
        test if input is a string
        '''
        self.assertRaises(TypeError,self.signup.fname)
        self.assertRaises(TypeError,self.signup.lname)
        self.assertRaises(TypeError,self.signup.emails)

    def test_few_characters(self):
        '''
        Test if inputs are enough characters
        '''
        self.assertTrue(self.signup.fname)
        self.assertTrue(self.signup.lname)
        self.assertTrue(self.signup.emails)

    def test_for_valid_email(self):
        '''
        Test for a valid email address
        '''
        self.assertIn('@', self.signup.emails["mail"])

    def test_email_invalid(self):
        self.assertNotEqual(self.signup.emails["mail"],"kasule@gmail")
    