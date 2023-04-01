import openai
import pyfiglet


class ChatGPT:
    def __init__(self):
        openai.api_key = ""
        self.model_engine = "text-davinci-003"

    def respond_to_prompt(self, prompt):
        response = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=100)
        text = response.choices[0].text.strip()
        return text

    def change_model_engine(self, model_engine):
        self.model_engine = model_engine


def enter_user_prompt():
    variable = input('>>')
    response = gpt_instance.respond_to_prompt(variable)
    print(response)
    enter_user_prompt()


if __name__ == "__main__":
    ascii_banner = pyfiglet.figlet_format("ChatGPT")
    print(ascii_banner)
    gpt_instance = ChatGPT()
    enter_user_prompt()
