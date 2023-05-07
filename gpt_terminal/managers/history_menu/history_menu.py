from gpt_terminal.managers.history_menu.history_settings import History


class HistoryMenu:
    def __init__(self):
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

    def load_conversation(self, conversation_name):
        conversation = self.history_settings.load_history(conversation_name)
        print(f"Loading conversation : {conversation_name}")
        print(conversation)

    def print_conversation(self, conversation_name):
        conversation = self.history_settings.load_history(conversation_name)
        print(f"Loading conversation : {conversation_name}")
        print(conversation)

    def save_conversation_to_file(self):
        pass

    def delete_conversation(self, conversation_name):
        self.history_settings.delete_conversation(conversation_name)
        print(f"Deleted the conversation : {conversation_name}")