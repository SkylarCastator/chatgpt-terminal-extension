from gpt_terminal.managers.history_menu.history_settings import History
import gpt_terminal.prompt_ui.dropdownmenu as dropdownmenu


class HistoryMenu:
    def __init__(self, terminal_instance):
        self.terminal_instance = terminal_instance
        self.history_settings = History()

    def list_all_conversations(self):
        arr = self.history_settings.list_history_files()
        print("This is a list of all previously saved conversations")
        if len(arr) > 0:
            for file_name in arr:
                name = file_name.replace(".json", "")
                print(name)
        else:
            print("No previous conversations were found")

    def load_conversation(self):
        options = self.history_settings.list_history_files()
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        conversation = self.history_settings.load_history(options[menu_entry_index].replace(".json", ""))
        print(conversation)
        prompt_name = options[menu_entry_index].replace(".json", "")
        print(f"Loading conversation : {options[menu_entry_index]}")
        for response in self.history_settings.parse_conversation(conversation):
            print(response)
            print("\n")
        self.terminal_instance.load_previous_conversation(prompt_name, conversation)

    def print_path(self):
        print("Path to History Files: ")
        print(self.history_settings.get_history_path())

    def print_conversation(self):
        options = self.history_settings.list_history_files()
        selected_item = dropdownmenu.dropdown_menu(options)

        conversation = self.history_settings.load_history(selected_item.replace(".json", ""))
        print(f"Loading conversation : {selected_item}")
        for response in self.history_settings.parse_conversation(conversation):
            print(response)
            print("\n")

    def delete_conversation(self):
        options = self.history_settings.list_history_files()
        selected_item = dropdownmenu.dropdown_menu(options)

        self.history_settings.delete_conversation(selected_item.replace(".json", ""))
        print(f"Deleted the conversation : {selected_item}")
