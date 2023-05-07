import json
import os
from gpt_terminal import platform_helper


class UserData:
    def __init__(self):
        self.chatgpt_token = ""

        project_path = f"{platform_helper.get_appdata_folder()}/GPT-Terminal/"
        if not os.path.exists(project_path):
            os.mkdir(project_path)
        self.user_data_path = f"{project_path}user_pref.json"


    def check_user_file_exists(self):
        """
        Checks if there is a user file
        :return: (boolean) Returns result if path exists or not.
        """
        if os.path.exists(self.user_data_path):
            return True
        else:
            return False

    def load_user_data(self):
        """
        Loads the user data to run the gpt_terminal
        """
        if os.path.exists(self.user_data_path):
            with open(self.user_data_path, 'r') as f:
                data = json.load(f)
                self.chatgpt_token = data["chatgpt_token"]
                f.close

    def get_user_data_json(self):
        """
        Returns a string of the context in the User Preferences
        :return: Returns a string of the json data
        """
        if os.path.exists(self.user_data_path):
            with open(self.user_data_path, 'r') as f:
                data = json.load(f)
                f.close
        else:
            return "No file found for user preferences"
        return data

    def write_user_data_file(self):
        """
        Writes the user data to manage the user's personal data
        """
        userdata = {
            "chatgpt_token":self.chatgpt_token
        }
        with open(self.user_data_path, 'w') as json_file:
            json.dump(userdata, json_file, indent=4, sort_keys=True)
            json_file.close()
