import uuid

class User(object):

    def __init__(self, username, password, name, email):
        self.uuid = uuid.uuid4()
        self.username = username
        self.password = password
        self.name = name
        self.email = email

