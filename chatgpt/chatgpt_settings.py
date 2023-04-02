import json
import os
import platform_helper


class ChatGPTData:
    def __init__(self):
        self.model_engine = "text-davinci-003"
        self.max_tokens = 100

        project_path = f"{platform_helper.get_appdata_folder()}/GPT-Terminal/"
        if not os.path.exists(project_path):
            os.mkdir(project_path)
        self.gpt_data_path = f"{project_path}chatgpt_pref.json"

        if os.path.exists(self.gpt_data_path):
            self.load_gpt_data()
        else:
            self.write_gpt_data_file()

    def load_gpt_data(self):
        """
        Loads the chatgpt data to run the application
        """
        if os.path.exists(self.gpt_data_path):
            with open(self.gpt_data_path, 'r') as f:
                data = json.load(f)
                self.model_engine = data["model-engine"]
                self.max_tokens = data["max-tokens"]
                f.close

    def get_gpt_data_json(self):
        """
        Returns a string of the context in the GPT Preferences
        :return: Returns a string of the json data
        """
        if os.path.exists(self.gpt_data_path):
            with open(self.gpt_data_path, 'r') as f:
                data = json.load(f)
                f.close
        else:
            return "No file found for gpt preferences"
        return data

    def write_gpt_data_file(self):
        """
        Writes the chatgpt data to manage the user's personal data
        """
        gpt_data = {
            "model-engine": self.model_engine,
            "max-tokens": self.max_tokens
        }
        with open(self.gpt_data_path, 'w') as json_file:
            json.dump(gpt_data, json_file, indent=4, sort_keys=True)
            json_file.close()
