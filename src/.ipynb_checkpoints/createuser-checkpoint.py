class UserModule:
    
    def __init__(self, allusers):
        self.users = allusers
        self._login_user = None
    def create_user(self):
        name = input("Enter your Name")
        email = input('Enter your Email')
        password = input("Enter a password")
        address = input('Enter your complete Address')
        country = input("Enter your Country Name")
        city = input('Enter your City Name')
        cnic = input("Enter your cnic Name")
    
        userData = {"name": name, "email": email, "address": address, "country": country, "city": city, "cnic": cnic, 'password': password}
        self.users.append(userData)
        return userData

    def get_users(self):
        return self.users

    def login_user(self):

        email = input("Enter email")
        password = input('Enter password')
        print(password)
        for user in self.users:
            if email == user['email'] and password == user['password']:
                print('userlogin successfully', user)
                self._login_user = user
                return user
        print('Incorrect credentials')
        return False

    def get_login_user(self):
        return self._login_user

    def forgot_password(self):
        email = input("Enter your email")
        for user in self.users:
            if email == user['email']:
                new_password = input("Enter your new password")
                user['password'] = new_password
                print('Password updated successfully')
                return True
                
        print('Incorrect credentials')
        return False