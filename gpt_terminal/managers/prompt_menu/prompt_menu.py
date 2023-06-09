import json
import os
import gpt_terminal.prompt_ui.dropdownmenu as dropdownmenu
from gpt_terminal.managers.prompt_menu.prompts_settings import PromptSettings


class PromptMenu:
    def __init__(self, terminal_instance):
        self.terminal_instance = terminal_instance
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
        selected_item = dropdownmenu.dropdown_menu(options)
        selected_prompt = self.prompt_settings.get_prompt_content(selected_item)
        prompt_name = selected_item
        prompt_name = prompt_name.replace(" ", "_")
        prompt_name = prompt_name.lower()
        print(f"Loading conversation : {selected_item}")
        print(f"{selected_prompt}\n")
        self.terminal_instance.call_llm_response(selected_prompt, prompt_name)
        self.terminal_instance.enter_user_prompt(self.terminal_instance.interface)


