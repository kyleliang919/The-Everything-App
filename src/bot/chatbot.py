import time
import random
import warnings
import undetected_chromedriver as uc

class Chatbot(object):
    def __init__(self):
        self.driver = uc.Chrome()
        # this will pop up a chrome showing the login, follow the steps to login manually
        self.driver.get('https://chat.openai.com/chat')
        self.textarea = None
        self.button = None
        while self.button is None and self.textarea is None:
            self.verify_login()
            time.sleep(random.randint(2, 10))

    def get_textarea_and_button(self):
        try:
            self.textarea = self.driver.find_element("tag name", "textarea")
            self.button = self.driver.find_element("xpath", "/html/body/div/div/div/main/div[2]/form/div/div[2]/button")
        except:
            self.textarea = None
            self.button = None
            return

    def verify_login(self):
        # grabbing the text input area and the send button on the chat interface
        self.get_textarea_and_button()
        if self.textarea is None or self.button is None:
            warnings.warn("you are not on the right page, please login in the browser and proceed to the right page")

    def verify_response_loading(self):
        last_page_source = self.driver.page_source
        while True:
            time.sleep(1) # This time is necessary because Ajax response, in case the response is not fully generated, 2 minutes should be generous enough
            if len(self.driver.page_source) != len(last_page_source):
                continue
            else:
                break

    def get_chat_response(self, prompt):
        if len(prompt) == 0:
            response["message"] = "Please input nonempty prompt!"
            return response
        response = {"message": None, "code_gen": None, "list_gen": None}
        self.get_textarea_and_button()
        try:
            self.textarea.send_keys(prompt)
            self.button.click()
            self.verify_response_loading()
            total_num = len(self.driver.find_elements("xpath", "/html/body/div/div/div[1]/main/div[1]/div/div/div/div")) - 1
            latest_xpath_prefix = "/html/body/div/div/div[1]/main/div[1]/div/div/div/div" + f"[{total_num}]"
            list_of_code_gen = self.driver.find_elements("xpath", latest_xpath_prefix + "//pre")
            if len(list_of_code_gen) == 0:
                response["message"] = self.driver.find_elements("xpath", latest_xpath_prefix + "//p")[0].text
            elif len(list_of_code_gen) == 1:
                code_gen = "# " + self.driver.find_elements("xpath", latest_xpath_prefix + "//pre")[0].text
                response["code_gen"] = code_gen
            else:
                response["message"] = "chatgpt: More than one block of code is generated, please make sure only one block is generated by prompting (ex. Adding a prefix: 'Answer in code only:')"
            list_of_list_gen = self.driver.find_elements("xpath", latest_xpath_prefix + "//li")
            if len(list_of_list_gen) == 0:
                pass
            else:
                response["list_gen"] = [each.text for each in list_of_list_gen]    
        except:
            response["message"] = "Failed to locate chat box on the page, please make sure you are on the right page."
        return response
