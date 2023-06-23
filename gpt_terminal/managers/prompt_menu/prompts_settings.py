import json
import os


class PromptSettings:
    def __init__(self):
        self.prompt_data = self._load()

    def list_all(self):
        arr = []
        for key in self.prompt_data.keys():
            arr.append(key)
        return arr

    def _load(self):
        with open("prompts.json", "r") as f:
            return json.load(f)

    def get_prompt_content(self, prompt_key):
        return self.prompt_data[prompt_key]["prompt"]

