import string
import random

class System:
    def __init__(self):
        self._users = {}

    def user_exists(self, username):
        return username in self._users

    def create_user(self, first_name, last_name, username):
        if self.user_exists(username):
            print('User exists!')
            return False

        # Create user if it does not already exist
        user = User(first_name, last_name, username)
        self._users[username] = user
        print('Created {} successfully'.format(user.username))

        return True

    def remove_user(self, username):
        if self.user_exists(username):
            self._users.pop(username)
            print('Deleted {} successfully'.format(username))
        else:
            print('User does not already exist!')

    def change_name(self, first_name, last_name, username):
        if self.user_exists(username):
            user = self._users[username]
            user.first_name = first_name
            user.last_name = last_name
            print('Name for {} was successfully changed to {} {}'.format(username, first_name, last_name))
        else:
            print('User does not already exist!')

class User:
    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = self._generate_password()

    def _generate_password(self):
        length = 4

        # Choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        
        return result_str