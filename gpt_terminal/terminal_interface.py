from gpt_terminal.chatgpt.chatgpt import ChatGPT
from gpt_terminal.preferences.userdata_settings import UserData
import pyfiglet
import gpt_terminal.prompt_ui.history_menu as history_menu
import gpt_terminal.prompt_ui.model_menu as model_menu
import gpt_terminal.prompt_ui.template_menu as template_menu
import gpt_terminal.prompt_ui.user_menu as user_menu


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

    def compile_menu_interfaces(self):
        menus = []
        for menu in menus:
            with open(menu, "r") as f:
                data = json.load(f)
                menu_items = []
                for menu_item in data["menu_items"]:
                    menu_items.append(MenuItem(menu_item["name"], menu_item["prompt"], menu_item["log_message"], menu_item["help_message"], menu_item["function"]))
                self.menu_data = data


    class MenuInterface:
        def __init__(self, ):
            print("Menu Interface")
            self.menu_class = None
            self.menu_data = ""
            self.menu_items = []

        def parse_menu(self):
            filename = "menu.json"
            with open(filename, "r") as f:
                data = json.load(f)
                for menu_item in data["menu_items"]:
                    self.menu_items.append(self.MenuItem(menu_item["name"], menu_item["prompt"], menu_item["log_message"], menu_item["help_message"], menu_item["function"]))
                self.menu_data = data

    class MenuItem:
        def __init__(self, name, prompt, log_message, help_message, function):
            self.name = name
            self.prompt = prompt
            self.log_message = log_message
            self.help_message = help_message
            self.function = function

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
        if variable == ":help":
            print("""
            ChatGPT Application Help Menu :
                :help : Loads the help menu
                :user : Allows the user to edit their preferences and tokens
                :history :Allows the user to aceess previous chat history
                :template : Allows the user to edit the templates for the chatgpt
                :chatgpt : Allows the user to change the settings for ChatGPT
                :exit : Exits the Application""")
            self.enter_user_prompt()
        elif variable == ":user":
            print("""
            Enter a User Setting to edit :
                :display : Displays the full content of the setting file
                :chatgpt_token : Edits the ChatGPT Token
                :exit : Exits the user setting prompt""")
            self.set_user_pref_prompt()
        elif variable == ":chatgpt":
            print("""
            Enter a ChatGPT setting to edit:
                :display : Displays the full content of the settings file
                :exit : Exits the ChatGPT settings prompt""")
            self.set_chatgpt_pref_prompt()
        elif variable == ":exit":
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
        if variable == ":display":
            print(self.gpt_instance.gpt_settings.get_gpt_data_json())
            self.set_chatgpt_pref_prompt()
        elif variable == ":exit":
            self.enter_user_prompt()
        else:
            print("Not a valid input. enter /exit to get back into regular prompt")
            self.set_chatgpt_pref_prompt()

    def set_user_pref_prompt(self):
        """
        Settings prompt to edit User Preferences
        """
        variable = input('User Settings >>')
        if variable == ":display":
            print(self.user_data.get_user_data_json())
            self.set_user_pref_prompt()
        elif variable == ":chatgpt-key":
            self.prompt_for_chatgpt_token()
        elif variable == ":exit":
            self.enter_user_prompt()
        else:
            print("Not a valid input. enter /exit to get back into regular prompt")
            self.set_user_pref_prompt()

    def prompt_editor(self, prompt):
        variable = input('Template Editor >>')
        if variable == ":new":
            print("Enter the text for the new template")
            print("Enter Given Arguments for template")
        elif variable == ":edit":
            print("Enter the name of the template to edit")
        elif variable == ":delete":
            print("Enter the name of the template to delete")
        elif variable == ":display":
            print("List of Templates:")
        elif variable == ":exit":
            self.enter_user_prompt()
        else: 
            print("Not a valid input. enter /exit to get back into regular prompt")
            self.prompt_editor(prompt)
