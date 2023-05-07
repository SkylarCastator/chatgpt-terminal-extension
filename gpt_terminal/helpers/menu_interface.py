class MenuInterface:
    def __init__(self,
                 name="",
                 prompt="",
                 log_message="",
                 help_message="",
                 error_message="",
                 prompt_header="",
                 class_ref="",
                 func_call="",
                 menu_items={}):
        self.name = name
        self.prompt = prompt
        self.log_message = log_message
        self.help_message = help_message
        self.error_message = error_message
        self.prompt_header = prompt_header
        self.class_ref = class_ref
        self.func_call = func_call
        self.menu_items = menu_items



