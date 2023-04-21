import json
import os

class TemplateHelper:
    def __init__(self, filename):
        self.filename = filename

    class Template:
        def __init__(self, text="", args=[]):
            self.text = text
            self.args = args

    def save(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f)

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        else:
            return None
