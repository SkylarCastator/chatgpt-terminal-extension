
class ModelMenu:
    def __init__(self, model_data):
        self.model_data = model_data

    def display_model_settings(self):
        print("Model Settings : ")
        print(self.model_data.get_gpt_data_json())