from chatgpt.chatgpt import ChatGPT
from userdata_settings import UserData
import pyfiglet


class TerminalInterface:
    def __init__(self):
        ascii_banner = pyfiglet.figlet_format("ChatGPT")
        print(ascii_banner)
        user_data = UserData()
        user_data.load_user_data()
        self.gpt_instance = ChatGPT(user_data.chatgpt_token)
        self.enter_user_prompt()

    def enter_user_prompt(self):
        """
        Recursive function to call for the user prompt to be entered into ChatGPT
        """
        variable = input('>>')
        if variable == "/help":
            print("""
            ChatGPT Application Help Menu :
                /help : Loads the help menu
                /user : Allows the user to edit their preferences and tokens
                /chatgpt : Allows the user to change the settings for ChatGPT
                /exit : Exits the Application""")
            self.enter_user_prompt()
        elif variable == "/user":
            print("""
            Enter a User Setting to edit :
                /display : Displays the full content of the setting file
                /chatgpt_token : Edits the ChatGPT Token
                /exit : Exits the user setting prompt""")
            self.set_user_pref_prompt()
        elif variable == "/chatgpt":
            print("""
            Enter a ChatGPT setting to edit:
                /display : Displays the full content of the settings file
                /exit : Exits the ChatGPT settings prompt""")
            self.set_chatgpt_pref_prompt()
        elif variable == "/exit":
            exit()
        else:
            response = self.gpt_instance.respond_to_prompt(variable)
            print(response)
            self.enter_user_prompt()

    def set_chatgpt_pref_prompt(self):
        """
        Settings prompt menu to change the preferences for ChatGPT
        """
        variable = input('chatgpt-settings >>')
        if variable == "/display":
            print("{Some json file}")
            self.set_chatgpt_pref_prompt()
        elif variable == "/exit":
            self.enter_user_prompt()
        else:
            print("Not a valid input. enter /exit to get back into regular prompt")
            self.set_chatgpt_pref_prompt()

    def set_user_pref_prompt(self):
        """
        Settings propmt to edit User Preferences
        """
        variable = input('user-settings >>')
        if variable == "/display":
            print("{Some json file}")
            self.set_user_pref_prompt()
        elif variable == "/exit":
            self.enter_user_prompt()
        else:
            print("Not a valid input. enter /exit to get back into regular prompt")
            self.set_user_pref_prompt()
