import time
import random
import warnings
import copy
import openai
import re

class ChatbotWrapper(object):
    def __init__(self, credentials):
        openai.api_key = credentials["openai"]["api_key"]
        openai.organization = credentials["openai"]["organization"]
        self.code_buffer = None
        self.credentials = credentials

    def parse_app_name_updated(self, prompt):
        response = self.get_chat_response("Answer in a single word, What App could finish the following task: " + prompt + " in the following apps " + str(self.credentials.keys()), internal_call = True)['message'] 
        return re.sub(r'\W+', '', response).lower() 

    def get_chat_response(self, prompt, app = "", internal_call = False):
        response = {"message": None, "code_gen": None, "list_gen": None}
        if len(prompt) == 0:
            response["message"] = "Please input nonempty prompt!"
            return response
        else:
            updated_prompt = prompt 
            if len(app) > 0 and app in self.credentials.keys():
                prefix = "Use " + str(self.credentials[app])
                updated_prompt = prefix + " to generate a python api call to " + prompt
            raw_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": updated_prompt},
                ]
            )
            raw_response = [each["message"]["content"] for each in raw_response["choices"]]
            if len(raw_response) == 0:
                response["message"] = "I am currently not avaliable, please check back later."
            else:
                response["message"] = raw_response[-1]
            try:
                response["code_gen"] = re.search('```python\n((.|\n)*)```', response["message"]).group(1)
                if response["code_gen"] is None:
                   response["code_gen"] = re.search('```((.|\n)*)```', response["message"]).group(1) 
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

        filled_code = self.code_buffer
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