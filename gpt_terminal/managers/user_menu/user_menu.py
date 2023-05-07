class UserMenu:
    def __init__(self, user_data):
        self.user_data = user_data

    def display_user_settings(self):
        print("User's Settings : ")
        print(self.user_data.get_user_data_json())

