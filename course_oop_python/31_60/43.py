def hash_function(password):
    pass

class Account:
    def __init__(self, login, password):
        self._login = login
        self._password = hash_function(password)

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        raise AttributeError('Изменение логина невозможно')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = hash_function(new_password)

