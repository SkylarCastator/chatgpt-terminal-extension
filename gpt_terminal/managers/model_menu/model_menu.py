from gpt_terminal.managers.model_menu.chatgpt_settings import ChatGPTData


class ModelMenu:
    def __init__(self):
        self.model_data = ChatGPTData()

    def display_model_settings(self):
        print("Model Settings : ")
        print(self.model_data.get_gpt_data_json())