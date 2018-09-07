import unittest
from signUp import SignUp
class SignUpTest(unittest.TestCase):

    def test_signup_creation(self):
        signup = SignUp()
        self.assertIsInstance(signup, SignUp)
    def test_add_user(self):
        signup = SignUp()
        signup.add("john doe", "john@gmail.com")
        self.assertEquals(len(signup.user_bio),1)

    def test_return_password(self):
        signup = SignUp()
        signup.add("john", "12345")
        self.assertEqual(signup.get_password("john"), "12345")

    def test_missing_key(self):
        signup = SignUp()
        with self.assertRaises(KeyError):
            signup.get_password("jo")

    def test_length_of_bio(self):
        signup = SignUp()
        signup.user_bio("john doe", "john@gmail.com")
        self.assertEqual(len(signup.user_bio), 7)

    # skip test
    # @unittest.skip(WIP)
    # def test_unknown()