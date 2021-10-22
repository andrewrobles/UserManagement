import unittest

from system import System

class TestScripts(unittest.TestCase):
    
    def setUp(self):
        self.system = System()

    def test_user_exists(self):
        result = self.system.user_exists('username')
        self.assertFalse(result)

    def test_create_user(self):
        is_success = self.system.create_user('first', 'last', 'username')
        result = self.system.user_exists('username')

        self.assertTrue(result)
        self.assertTrue(is_success)

        # Verify no duplicate usernames are created
        self.assertEqual(len(self.system._users), 1)
        is_success = self.system.create_user('first', 'last', 'username')
        self.assertFalse(is_success)

        # Verify multiple users can be created
        is_success = self.system.create_user('first', 'last', 'differentusername')
        self.assertTrue(is_success)

    def test_remove_user(self):
        self.assertEqual(len(self.system._users), 0)
        self.system.create_user('first', 'last', 'username')
        self.assertEqual(len(self.system._users), 1)

        self.system.remove_user('nonexistentusername')
        self.assertEqual(len(self.system._users), 1)

        self.system.remove_user('username')
        self.assertEqual(len(self.system._users), 0)

    def test_change_name(self):
        self.system.create_user('oldfirstname', 'oldlastname', 'username')

        user = self.system._users['username']
        self.assertEqual(user.first_name, 'oldfirstname')
        self.assertEqual(user.last_name, 'oldlastname')
        self.assertEqual(len(user.password), 4)

        self.system.change_name('newfirstname', 'newlastname', 'username')
        self.assertEqual(user.first_name, 'newfirstname')
        self.assertEqual(user.last_name, 'newlastname')
        

if __name__ == '__main__':
    unittest.main()