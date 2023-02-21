import time
import random
import warnings
import copy
from revChatGPT.V1 import Chatbot
import re

class ChatbotWrapper(object):
    def __init__(self, credentials):
        self.chatbot = Chatbot(config=credentials["openai"])
        self.code_buffer = None
        self.credentials = credentials

    def get_chat_response(self, prompt, internal_call = False):
        response = {"message": None, "code_gen": None, "list_gen": None}
        if len(prompt) == 0:
            response["message"] = "Please input nonempty prompt!"
            return response
        else:
            raw_response = self.chatbot.ask(
                prompt,
                conversation_id=self.chatbot.config.get("conversation"),
                parent_id=self.chatbot.config.get("parent_id"),
            )
            response["message"] = [each for each in raw_response][-1]["message"]
            try:
                response["code_gen"] = re.search('```python\n((.|\n)*)```', response["message"]).group(1)
            except:
                pass
            if not internal_call:
                self.code_buffer = response["code_gen"]
            return response

    def parse_app_name(self):
        response = self.get_chat_response("Answer in a single word: What App was the script for?", internal_call = True)['message']
        return re.sub(r'\W+', '', response).lower()

    def parse_and_execute(self):
        if self.code_buffer is None:
            warnings.warn(f"chatgpt: no code generation is detected.")
            return
        app_name = self.parse_app_name()
        if app_name in self.credentials.keys():
            if app_name not in self.credentials:
                filled_code = None
            else:
                filled_code = self.get_chat_response("Replace keys in the code with values in the following dictionary:"+str(self.credentials[app_name]))["code_gen"]
        else:
            warnings.warn(f"chatgpt: This app has not been supported! You are welcome to contribute to the repo by adding the app.")
            return

        for i in range(3):
            print("chatgpt:\n"+filled_code)
            if filled_code is not None:
                try:
                    exec(filled_code)
                    print(f"chatgpt: code executed, please check app for results")
                    return
                except Exception as e:
                    filled_code = self.get_chat_response("fix the error:" + str(e))["code_gen"]
                    print(f"chatgpt: execution failed, retrying " + str(i) + "th times")
                    if i == 2:
                        return
        
