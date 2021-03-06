import functools

user={"username":"jose", "access_level":"guest"}

def make_secure(func):
    @functools.wraps(func) 
    def secure_function(*args, **kwargs): #so that it is generic
        if user["access_level"]=="admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function

@make_secure
def get_admin_password(panel):
    if panel=="admin":
        return "1234"
    elif panel=="billing":
        return "super_secure_password"


#user={"username":"jose", "access_level":"admin"}

print(get_admin_password.__name__)
print(get_admin_password())

