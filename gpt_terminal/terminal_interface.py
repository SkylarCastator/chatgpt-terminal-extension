from gpt_terminal.chatgpt.chatgpt import ChatGPT
from gpt_terminal.preferences.userdata_settings import UserData
import pyfiglet


class TerminalInterface:
    def __init__(self):
        ascii_banner = pyfiglet.figlet_format("ChatGPT")
        print(ascii_banner)
        self.user_data = UserData()
        if self.user_data.check_user_file_exists():
            self.user_data.load_user_data()
            self.gpt_instance = ChatGPT(self.user_data.chatgpt_token)
            connection = self.gpt_instance.test_chatgpt_connection()
            if connection:
                self.enter_user_prompt()
            else:
                print("The connection to ChatGPT could not be created. Make sure you are connected to the internet or have the correct key")
        else:
            self.user_data.write_user_data_file()
            self.prompt_onboarding()

    def prompt_onboarding(self):
        self.user_data.write_user_data_file()
        print("""
        Welcome to ChatGPT Terminal App
        We need to connect a ChatGPT key to the gpt_terminal.
        Use the link https://platform.openai.com/account/api-keys to get the key and enter it in the prompt.""")
        self.prompt_for_chatgpt_token()

    def prompt_for_chatgpt_token(self):
        variable = input('Set ChatGPT Key >>')
        if variable == "":
            print("Please enter a valid key for ChatGPT")
            self.prompt_for_chatgpt_token()
        else:
            self.gpt_instance = ChatGPT(variable)
            connection_result = self.gpt_instance.test_chatgpt_connection()
            if connection_result:
                self.user_data.chatgpt_token = variable
                self.user_data.write_user_data_file()
                print("Connection Completed. Start ChatGPT by entering a prompt")
                self.enter_user_prompt()
            else:
                print("Failed to connect to ChatGPT, make sure you are using the correct key.")
                self.prompt_for_chatgpt_token()

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
        variable = input('ChatGPT Settings >>')
        if variable == "/display":
            print(self.gpt_instance.gpt_settings.get_gpt_data_json())
            self.set_chatgpt_pref_prompt()
        elif variable == "/exit":
            self.enter_user_prompt()
        else:
            print("Not a valid input. enter /exit to get back into regular prompt")
            self.set_chatgpt_pref_prompt()

    def set_user_pref_prompt(self):
        """
        Settings prompt to edit User Preferences
        """
        variable = input('User Settings >>')
        if variable == "/display":
            print(self.user_data.get_user_data_json())
            self.set_user_pref_prompt()
        elif variable == "/chatgpt-key":
            self.prompt_for_chatgpt_token()
        elif variable == "/exit":
            self.enter_user_prompt()
        else:
            print("Not a valid input. enter /exit to get back into regular prompt")
            self.set_user_pref_prompt()
