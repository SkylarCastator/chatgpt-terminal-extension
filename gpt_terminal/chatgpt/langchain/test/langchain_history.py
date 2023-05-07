from langchain.memory import ChatMessageHistory
from langchain.schema import messages_from_dict, messages_to_dict
import json

def save_history(history):
    with open("history.json", "w") as f:
        json.dump(messages_to_dict(history.messages), f)

def load_history(filename="history"):
    with open(f"{filename}.json", "r") as f:
        dict = json.load(f)
        return messages_from_dict(dict)

if __name__ == "__main__":
    chat_history = ChatMessageHistory()
    chat_history.add_user_message("Hello")
    chat_history.add_ai_message("Hi")
    print(chat_history.messages)
    save_history(chat_history)
    print(load_history())
