import openai
from gpt_terminal.managers.model_menu.chatgpt_settings import ChatGPTData
from langchain.memory import ChatMessageHistory
from gpt_terminal.managers.history_menu.history_settings import History
from langchain.schema import messages_from_dict, messages_to_dict


class ChatGPT:
    def __init__(self, api_key):
        if api_key == "":
            print("The API key was not set properly use the /help menu to debug")
            return

        self.gpt_settings = ChatGPTData()
        openai.api_key = api_key
        self.model_engine = "gpt-3.5-turbo"

        self.conversation_prompt_summary = ""
        self.chat_history = ChatMessageHistory()
        self.history_manager = History()

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
        except Exception as e:
            print("Failed to connect : " + str(e))
            return False

    def respond_to_prompt(self, prompt, prompt_name=""):
        """
        Sends a prompt to ChatGPT and waits for a response
        :param prompt_name: Name of the prompt for loading prompt data
        :param prompt: The Prompt to run in ChatGPT
        :return: Returns the string of ChatGPT response
        """
        if prompt_name != "":
            self.conversation_prompt_summary = prompt_name
            self.chat_history = ChatMessageHistory()
        if self.conversation_prompt_summary == "":
            self.create_summary_title_for_conversation(prompt)
        self.chat_history.add_user_message(prompt)

        messages = []
        for message in messages_to_dict(self.chat_history.messages):
            if message["type"] == "human":
                role = "user"
            else:
                role = "assistant"
            messages.append({"role": role, "content": message["data"]["content"]})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        text = response['choices'][0]['message']['content']
        self.chat_history.add_ai_message(text)
        self.history_manager.save_history(self.chat_history, self.conversation_prompt_summary)
        return text

    def load_conversation(self, conversation_name, chat_history):
        self.chat_history = ChatMessageHistory()
        self.conversation_prompt_summary = conversation_name

        messages = []
        for message in chat_history:
            if message["type"] == "human":
                role = "user"
            else:
                role = "assistant"
            messages.append({"role": role, "content": message["data"]["content"]})

        for message in chat_history:
            if message["type"] == "human":
                self.chat_history.add_user_message(message["data"]["content"])
            else:
                self.chat_history.add_ai_message(message["data"]["content"])

        messages.append({"role": "user", "content": "Please say 'Ready'"})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        reply = response['choices'][0]['message']['content']
        return reply

    def create_summary_title_for_conversation(self, prompt):
        response = openai.Completion.create(
            engine=self.gpt_settings.model_engine,
            prompt=f"Return a summarized name of this prompt to be used as a file : {prompt}",
            max_tokens=self.gpt_settings.max_tokens,
            temperature=0)
        summary = response.choices[0].text.strip()
        summary = summary.replace(".", "")
        self.conversation_prompt_summary = summary
