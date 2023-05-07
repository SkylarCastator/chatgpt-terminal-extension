import gpt_terminal.managers.user_menu.user_menu as user_menu
import gpt_terminal.managers.model_menu.model_menu as model_menu
import gpt_terminal.managers.history_menu.history_menu as history_menu


class MenuConfig:
    def __init__(self, terminal_interface):
        self.user_menu = user_menu.UserMenu(terminal_interface.user_data)
        self.model_menu = model_menu.ModelMenu()
        self.history_menu = history_menu.HistoryMenu()

    def return_menu_json_paths(self):
        return [
            "gpt_terminal/prompt_ui/managers/user_menu/user_menu.json",
            "gpt_terminal/prompt_ui/managers/model_menu/model_menu.json",
            "gpt_terminal/prompt_ui/managers/history_menu/history_menu.json"
        ]
