
class MenuInterface:
    def __init__(self, ):
        print("Menu Interface")
        self.menu_class = None
        self.menu_data = ""
        self.menu_items = []


class MenuItem:
    def __init__(self, name, prompt, log_message, help_message, function):
        self.name = name
        self.prompt = prompt
        self.log_message = log_message
        self.help_message = help_message
        self.function = function

