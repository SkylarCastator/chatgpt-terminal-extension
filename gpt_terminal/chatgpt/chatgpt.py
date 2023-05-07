import openai
from gpt_terminal.managers.model_menu.chatgpt_settings import ChatGPTData


class ChatGPT:
    def __init__(self, api_key):
        if api_key == "":
            print("The API key was not set properly use the /help menu to debug")
            return

        self.gpt_settings = ChatGPTData()
        openai.api_key = api_key
        self.model_engine = "text-davinci-003"

    def test_chatgpt_connection(self):
        """
        Tests the Chatgpt connection and returns result
        :return: (boolean) Returns if a connection could be made to ChatGPT
        """
        try:
            response = openai.Completion.create(
                engine=self.gpt_settings.model_engine,
                prompt="Hello",
                max_tokens=self.gpt_settings.max_tokens)
            text = response.choices[0].text.strip()
            return True
        except:
            return False

    def respond_to_prompt(self, prompt):
        """
        Sends a prompt to ChatGPT and waits for a response
        :param prompt: The Prompt to run in ChatGPT
        :return: Returns the string of ChatGPT response
        """
        response = openai.Completion.create(
            engine=self.gpt_settings.model_engine,
            prompt=prompt,
            max_tokens=self.gpt_settings.max_tokens,
            temperature=0)
        text = response.choices[0].text.strip()
        return text

