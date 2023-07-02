from gpt_terminal.chatgpt.chatgpt import ChatGPT
from gpt_terminal.managers.user_menu.userdata_settings import UserData
import pyfiglet
import json
from gpt_terminal.menu_interface import MenuInterface
import gpt_terminal.menu_config as menu_config


class TerminalInterface:
    def __init__(self):
        ascii_banner = pyfiglet.figlet_format("ChatGPT")
        print(ascii_banner)
        self.user_data = UserData()
        self.menus = {}
        self.interface = MenuInterface(
            name="Main Menu",
            prompt="",
            log_message="Welcome to TermChat, type :help to look at different menu options",
            help_message=" Welcome to the ChatGPT Terminal App Help Menu",
            error_message="That was not a correct prompt, use the :help command to find available prompts",
            prompt_header=">>",
            class_ref="",
            func_call="call_llm_response",
            menu_items={})

        self.menu_config = menu_config.MenuConfig(self)
        json_list = self.menu_config.return_menu_json_paths()

        self.compile_menu_interfaces(json_list, self.interface)

        if self.user_data.check_user_file_exists():
            self.user_data.load_user_data()
            self.gpt_instance = ChatGPT(self.user_data.chatgpt_token)
            self.test_connection()
        else:
            self.user_data.write_user_data_file()
            self.prompt_onboarding()

    def test_connection(self):
        connection = self.gpt_instance.test_chatgpt_connection()
        if connection:
            print(self.interface.log_message)
            self.enter_user_prompt(self.interface)
        else:
            print(
                "The connection to ChatGPT could not be created. Make sure you are connected to the internet or have the correct key")
            self.failed_to_connect_menu()

    def compile_menu_interfaces(self, json_list, parent_interface):
        for menu in json_list:
            with open(menu, "r") as f:
                data = json.load(f)
                interface = MenuInterface(
                    name=data["name"], 
                    prompt=data["prompt"],
                    log_message=data["log_message"],
                    help_message=data["help_message"],
                    error_message=data["error_message"],
                    prompt_header=data["prompt_header"],
                    class_ref=data["class"],
                    func_call=data["function"],
                    menu_items={})
                self.recursive_build_menu_tree(data["menu_items"], interface)
                self.menus[data["prompt_header"]] = interface
                parent_interface.menu_items[interface.prompt] = interface

    def recursive_build_menu_tree(self, parent_menu_items, parent_interface):
        for menu_item in parent_menu_items:
            menu_item_obj = MenuInterface(
                name=menu_item["name"], 
                prompt=menu_item["prompt"], 
                log_message=menu_item["log_message"], 
                help_message=menu_item["help_message"],
                error_message=menu_item["error_message"],
                prompt_header=menu_item["prompt_header"],
                class_ref=menu_item["class"],
                func_call=menu_item["function"],
                menu_items={})
            self.recursive_build_menu_tree(menu_item["menu_items"], menu_item_obj)
            parent_interface.menu_items[menu_item["prompt"]] = menu_item_obj

    def prompt_onboarding(self):
        self.user_data.write_user_data_file()
        print("""
        Welcome to ChatGPT Terminal App
        We need to connect a ChatGPT key to the gpt_terminal.
        Use the link https://platform.openai.com/account/api-keys to get the key and enter it in the prompt.""")
        self.prompt_for_chatgpt_token()

    def failed_to_connect_menu(self):
        print("""
        To retry your connection, type :retry
        To change the key, type :key
        To exit, type :exit""")
        variable = input('Connection Failed Menu >>')
        if variable == ":key":
            self.prompt_for_chatgpt_token()
        elif variable == ":retry":
            self.test_connection()
        elif variable == ":exit":
            exit()
        else:
            print("That was not a valid entry, try again.")
            self.failed_to_connect_menu()

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
                self.enter_user_prompt(self.interface)
            else:
                print("Failed to connect to ChatGPT, make sure you are using the correct key.")
                self.prompt_for_chatgpt_token()

    def enter_user_prompt(self, menu_system):
        print("\n")
        variable = input(menu_system.prompt_header)
        print("\n")
        if variable in menu_system.menu_items:
            if not menu_system.menu_items[variable].func_call == "":
                class_ref = getattr(self.menu_config, menu_system.menu_items[variable].class_ref)
                func_call = getattr(class_ref, menu_system.menu_items[variable].func_call)
                func_call()
                self.enter_user_prompt(menu_system)
                return
            if len(menu_system.menu_items[variable].menu_items) > 0:
                self.enter_user_prompt(menu_system.menu_items[variable])
        elif variable == ":exit":
            exit()
        elif variable == ":chat":
            self.enter_user_prompt(self.interface)
        elif variable == ":help":
            self.print_help_information(menu_system)
        else:
            if menu_system.func_call != "":
                func_call = getattr(self, menu_system.func_call)
                func_call(variable)
            else:
                print(menu_system.error_message)
            self.enter_user_prompt(menu_system)

    def print_help_information(self, menu_system):
        print(menu_system.log_message)
        for child in menu_system.menu_items:
            print(f"{menu_system.menu_items[child].prompt}    {menu_system.menu_items[child].help_message}")
        print(":chat    Goes to the the chat prompt")
        print(":exit    Exits the application")
        self.enter_user_prompt(menu_system)

    def call_llm_response(self, prompt, prompt_name=""):
        """
        Calls the LLM response function
        """
        response = self.gpt_instance.respond_to_prompt(prompt, prompt_name)
        print(response)

