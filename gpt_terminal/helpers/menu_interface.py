class MenuInterface:
    def __init__(self, name="", prompt="", log_message="", help_message="", prompt_header="", func_call="", menu_items={}):
        self.name = name
        self.prompt = prompt
        self.log_message = log_message
        self.help_message = help_message
        self.prompt_header = prompt_header
        self.func_call = func_call
        self.menu_items = menu_items



