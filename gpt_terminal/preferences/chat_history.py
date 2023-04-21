import json
import os
from gpt_terminal.helpers import platform_helper
from langchain.memory import ChatMessageHistory
from langchain.schema import messages_from_dict, messages_to_dict


class History:
    def __init__(self):
        project_path = f"{platform_helper.get_appdata_folder()}/GPT-Terminal/History/"
        if not os.path.exists(project_path):
            os.mkdir(project_path)
    
    def save_history(chat_history, file_name="history_0"):
        file_path = f"{self.project_path}/{file_name}
        with open(file_path, "w") as f:
            json.dump(messages_to_dict(history.messages), f)

    def load_history(filename="history_0"):
        file_path = f"{self.project_path}/{filename}"
        with open(f"{filename}.json", "r") as f:
            dict = json.load(f)
            return messages_from_dict(dict)

