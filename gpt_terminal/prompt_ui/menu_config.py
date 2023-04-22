import gpt_terminal.prompt_ui.menus.user_menu.user_menu as user_menu
import gpt_terminal.prompt_ui.menus.model_menu.model_menu as model_menu

class MenuConfig:
    def __init__(self, terminal_interface):
        self.user_menu = user_menu.UserMenu(terminal_interface.user_data)
        self.model_menu = model_menu.ModelMenu()

    def return_menu_json_paths(self):
        return [
            "gpt_terminal/prompt_ui/menus/user_menu/user_menu.json",
            "gpt_terminal/prompt_ui/menus/model_menu/model_menu.json"
        ]
