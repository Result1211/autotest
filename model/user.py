class User(object):

    def __init__(self, user_email=None, user_password=None):
        self.user_email = user_email
        self.user_password = user_password

    @classmethod
    def Admin(cls):
        return cls(user_email="test10@test.ru", user_password="tester10")