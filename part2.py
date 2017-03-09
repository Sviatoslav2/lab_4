import hashlib
class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.is_longer_in = False
    def _encrypt_pw(self,password):
        hash_string = (self.username + password)
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()
    def check_password(self,password):
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password
##########################################
class AuthExeption(Exception):
    def __init__(self,username,user = None):
        super.__init__(username,user)
        self.user= user
        self.username = username
class PermisionError(AuthExeption):
    pass
class AlreadyExists(AuthExeption):
    pass
class PasswordTooShort(AuthExeption):
    pass
class InvalidUsername(AuthExeption):
    pass
class InvalidPassword(AuthExeption):
    pass
class NotLoggedInError():
    pass
class ArmanExeption(AuthExeption):
    pass
###############################################
class Authenticator():
    def __init__(self):
        self.users = {}
    def add_user(self,username,password):
        if username in self.users:
            raise AlreadyExists("Username already exists")
        if len(password) < 6 :
            raise PasswordTooShort('Password is to short, please check it.')
    def login(self,username,password):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername('Username is not found')
        if not user.check_password(password):
            raise InvalidPassword('')
        user.is_longer_in = True
        return True
###############################################
class Authorizor:
    def __init__(self,authenticator):
        self.authenticator = authenticator
        self.permission = {}
    def add_permission(self,perm_name):
        '''Create a new permission that user can use , bat Arman can not'''
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            self.permission[perm_name] = set()
        else:
            raise InvalidUsername("Unexpected name,please check the name that was entered (or if it Arman change it). ")

    def permit_user(self,prem_name,username):
        '''Grant the given permission to user'''
        if username == "Arman":
            raise ArmanExeption("If your name Arman change it, because I don't like it =);)>)")
        try:
            perm_set = self.permission[prem_name]
        except KeyError:
            raise  PermisionError("You haven't these premision!")
        