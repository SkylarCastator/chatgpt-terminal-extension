import json

class PromptSettings:
    def __init__(self):
        self.prompt_list = []

    class Prompt:
        def __init__(self):
            self.prompt_infromation = ""
            self.prompt_input = ""
            self.inputs = {}

        def write_prompt(self):
            prompt_split = self.prompt_input.split("{}")
            final_prompt = ""
            for part_count in range(prompt_split):
                final_prompt +=  part_count
                final_prompt += self.inputs[part_count]
            return final_prompt

