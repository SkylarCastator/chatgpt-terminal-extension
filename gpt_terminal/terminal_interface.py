from gpt_terminal.chatgpt.chatgpt import ChatGPT
from gpt_terminal.preferences.userdata_settings import UserData
import pyfiglet
import json
from gpt_terminal.helpers.menu_interface import MenuInterface
import gpt_terminal.prompt_ui.menu_config as menu_config


class TerminalInterface:
    def __init__(self):
        ascii_banner = pyfiglet.figlet_format("ChatGPT")
        print(ascii_banner)
        self.user_data = UserData()
        self.menus = {}
        self.interface = MenuInterface(
            name="Main Menu",
            prompt="",
            log_message="Logging something here",
            help_message=" Welcome to the ChatGPT Terminal App Help Menu",
            prompt_header=">>",
            func_call="call_llm_response",
            menu_items={})

        self.menu_config = menu_config.MenuConfig(self)
        json_list = self.menu_config.return_menu_json_paths()
 
        self.compile_menu_interfaces(json_list, self.interface)

        if self.user_data.check_user_file_exists():
            self.user_data.load_user_data()
            self.gpt_instance = ChatGPT(self.user_data.chatgpt_token)
            connection = self.gpt_instance.test_chatgpt_connection()
            if connection:
                self.enter_user_prompt_2(self.interface)
            else:
                print("The connection to ChatGPT could not be created. Make sure you are connected to the internet or have the correct key")
        else:
            self.user_data.write_user_data_file()
            self.prompt_onboarding()

    def compile_menu_interfaces(self, json_list, parent_interface):
        for menu in json_list:
            with open(menu, "r") as f:
                data = json.load(f)
                interface = MenuInterface(
                    name=data["name"], 
                    prompt=data["prompt"],
                    log_message=data["log_message"],
                    help_message=data["help_message"],
                    prompt_header=data["prompt_header"],
                    func_call=data["function"],
                    menu_items={})
                interface.menu_items = self.recursive_build_menu_tree(data["menu_items"], interface)
                self.menus[data["prompt_header"]] = interface
                parent_interface.menu_items[interface.prompt] = interface

    def recursive_build_menu_tree(self, parent_menu_items, parent_interface):
        menu_items = {}
        for menu_item in parent_menu_items:
            menu_item_obj = MenuInterface(
                name=menu_item["name"], 
                prompt=menu_item["prompt"], 
                log_message=menu_item["log_message"], 
                help_message=menu_item["help_message"],
                prompt_header=menu_item["prompt_header"],
                func_call=menu_item["function"],
                menu_items={})
            menu_item_obj.menu_items = self.recursive_build_menu_tree(menu_item_obj.menu_items, menu_item_obj)
            parent_interface.menu_items["prompt_header"] = menu_item_obj

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
                self.enter_user_prompt_2(self.interface)
            else:
                print("Failed to connect to ChatGPT, make sure you are using the correct key.")
                self.prompt_for_chatgpt_token()

    def enter_user_prompt_2(self, menu_system):
        variable = input(menu_system.prompt_header)
        if variable in menu_system.menu_items:
            if not menu_system.menu_items[variable].func_calls == "":
               func_call = getattr(self.menu_config.user_menu, menu_system.menu_items[variable].func_calls)
            if len(menu_system.menu_items[variable].menu_items) > 0:
                self.enter_user_prompt_2(menu_system.menu_items[variable])
        elif variable == ":exit":
            exit()
        elif variable == ":help":
            print(menu_system.help_message)
            for child in menu_system.menu_items:
                print(menu_system.menu_items[child].help_message)
            self.enter_user_prompt_2(menu_system)
        else:
            if menu_system.func_call != "":
                func_call = getattr(self, menu_system.func_call)
                func_call()
            else:
                print(menu_system.log_message)
            self.enter_user_prompt_2(menu_system)

    #def enter_user_prompt(self):
    #    """
    #    Recursive function to call for the user prompt to be entered into ChatGPT
    #    """
    #    variable = input('>>')
    #    if variable == ":help":
    #        print("""
    #        ChatGPT Application Help Menu :
    #            :help : Loads the help menu
    #            :user : Allows the user to edit their preferences and tokens
    #            :history :Allows the user to aceess previous chat history
    #            :template : Allows the user to edit the templates for the chatgpt
    #            :chatgpt : Allows the user to change the settings for ChatGPT
    #            :exit : Exits the Application""")
    #        self.enter_user_prompt()
    #    elif variable == ":user":
    #        print("""
    #        Enter a User Setting to edit :
    #            :display : Displays the full content of the setting file
    #            :chatgpt_token : Edits the ChatGPT Token
    #            :exit : Exits the user setting prompt""")
    #        self.set_user_pref_prompt()
    #    elif variable == ":chatgpt":
    #        print("""
    #        Enter a ChatGPT setting to edit:
    #            :display : Displays the full content of the settings file
    #            :exit : Exits the ChatGPT settings prompt""")
    #        self.set_chatgpt_pref_prompt()
    #    elif variable == ":exit":
    #        exit()
    #    else:
    #        response = self.gpt_instance.respond_to_prompt(variable)
    #        print(response)
    #        self.enter_user_prompt()

    def call_llm_response(self):
        """
        Calls the LLM response function
        """
        response = self.gpt_instance.respond_to_prompt("Hello ChatGPT")
        print(response)

   # def set_chatgpt_pref_prompt(self):
   #     """
   #     Settings prompt menu to change the preferences for ChatGPT
   #     """
   #     variable = input('ChatGPT Settings >>')
   #     if variable == ":display":
   #         print(self.gpt_instance.gpt_settings.get_gpt_data_json())
   #         self.set_chatgpt_pref_prompt()
   #     elif variable == ":exit":
   #         self.enter_user_prompt()
   #     else:
   #         print("Not a valid input. enter /exit to get back into regular prompt")
   #         self.set_chatgpt_pref_prompt()

    #def set_user_pref_prompt(self):
    #    """
    #    Settings prompt to edit User Preferences
    #    """
    #    variable = input('User Settings >>')
    #    if variable == ":display":
    #        print(self.user_data.get_user_data_json())
    #        self.set_user_pref_prompt()
    #    elif variable == ":chatgpt-key":
    #        self.prompt_for_chatgpt_token()
    #    elif variable == ":exit":
    #        self.enter_user_prompt()
    #    else:
    #        print("Not a valid input. enter /exit to get back into regular prompt")
    #        self.set_user_pref_prompt()

