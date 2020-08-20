# this is login part if the user is already registered
from werkzeug .security import safe_str_cmp
from models.user import UserModel
# memory table with single user

def authenticate(username, password):   # this is username and password
    user = UserModel.find_by_username(username) # username is a key value, None is default
    #if user and user.password == password:
    if user and safe_str_cmp(user.password,password):   # safe string compare any version and return true if the strings are the same
        return user

def identify(payload):  # this is id section
    #payload is JWT content
    user_id = payload['identity']    # identity - this is user_id
    return UserModel.find_by_id(user_id)