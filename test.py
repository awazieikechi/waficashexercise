import unittest
from users import User

class TestUser(unittest.TestCase):

    def test_user_activation(self):
        user1 = User('User A')
        user2 = User('User B')
        self.assertEqual(user1.name, "User A")
        self.assertEqual(user2.name, "User B")
        self.assertTrue(user1.activate())
        self.assertTrue(user2.activate())

    def test_user_deposit(self):
        user1 = User('User A')
        user2 = User('User B')
        user1.deposit(10) 
        user2.deposit(20)
        self.assertEqual(user1.checkBalance(), 10)
        self.assertEqual(user2.checkBalance(), 20)

    def test_user_transfer(self):
        user1 = User('User A')
        user2 = User('User B')
        user1.account_balance = 10 
        user2.account_balance = 20
        User.transfer(user2, user1, 15)
        self.assertEqual(user1.checkBalance(), 25)
        self.assertEqual(user2.checkBalance(), 5)
    
    def test_user_withdraw(self):
        user1 = User('User A')
        user1.account_balance = 25 
        user1.withdraw(25)
        self.assertEqual(user1.checkBalance(), 0) 

if __name__ == '__main__':
    unittest.main()