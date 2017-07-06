import uuid

class User(object):

    def __init__(self, username, password, name, email):
        self.uuid = uuid.uuid4()
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __str__(self):
        return self.name + "(" + str(self.uuid) + ")"

    def __repr__(self):
        return self.name + "(" + str(self.uuid) + ")"

