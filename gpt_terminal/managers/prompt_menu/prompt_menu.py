import json
import os
from simple_term_menu import TerminalMenu
from gpt_terminal.managers.prompt_menu.prompts_settings import PromptSettings


class PromptMenu:
    def __init__(self):
        self.prompt_settings = PromptSettings()

    def list_all_prompts(self):
        arr = self.prompt_settings.list_all()
        print("This is a list of all Prompts")
        if len(arr) > 0:
            for prompt in arr:
                print(prompt)
        else:
            print("No previous conversations were found")

    def load_prompt(self):
        options = self.prompt_settings.list_all()
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        selected_prompt = self.prompt_settings.get_prompt_content(options[menu_entry_index])
        print(f"Loading conversation : {options[menu_entry_index]}")
        print(selected_prompt)
        #for response in self.history_settings.parse_conversation(conversation):
        #    print(response)
        #    print("\n")

