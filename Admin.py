class User():
    """ Describes a typical user"""

    def __init__(self, first_name, last_name, email, gender):
        """Instantiates a user"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.gender = gender
        self.login_attempts = 0
    def describe_user(self):
        """Describe a user"""
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Gender: {self.gender}")
    def greet_user(self):
        """Greeting a user"""
        msg_3 = f"Hello {self.first_name} {self.last_name}. How are you doing?"
        print(msg_3)

    def increment_login_attempts(self):
        '''Increments the number of attempts by 1'''
        self.login_attempts += 1


    def reset_login_attempts(self):
        '''Allows to reset the number of login attempts to 0'''
        self.login_attempts = 0

class Privileges():
    """Model the privileges of an admin"""

    def __init__(self, privileges_list = ["add and delete post", "remove and block users"]):
        self.privileges_list = privileges_list


    def show_privileges(self):
        """Print the privileges of an admin"""
        print("The administrator can:")
        for duty in self.privileges_list:
            print(f"- {duty}")


class Admin(User):
    """Child class inheriting from the Users class"""

    def __init__(self, first_name, last_name, email,  gender):
        """Initialize an admin"""
        super().__init__(first_name, last_name, email,  gender)
        self.privileges = Privileges()



admin = Admin("john", "doe", "john@aol.com", "male")

admin.privileges.show_privileges()


# user_1 = User("jean", "brière", "jbriere@aol.com", "black")
