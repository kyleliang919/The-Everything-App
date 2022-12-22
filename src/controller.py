import re
import apps
import warnings
def detect_code(response):
    results = re.findall(r'\`\`\`\n(.*?)\`\`\`\n', response, flags=re.S)
    if len(results) == 0:
        return None
    else:
        return results[0]

def parse_app_name(bot):
    response = bot.get_chat_response("Answer in a single word: What App was the script for?")['message']
    return re.sub(r'\W+', '', response).lower()

def parse_app_keys(bot):
    missing_key_list = bot.get_chat_response("Answer in a list of keys' names only: What keys were missing in the script?")['list_gen']
    return missing_key_list

def parse_and_execute(code_gen, credentials, bot):
    app_name = parse_app_name(bot)
    missing_key_list = parse_app_keys(bot)
    if app_name in dir(apps):
        if app_name not in credentials:
            filled_code = None
        else:
            filled_code = getattr(apps, app_name)(code_gen, credentials[app_name], missing_key_list)
    else:
        warnings.warn(f"chatgpt: This app has not been supported! You are welcome to contribute to the repo by adding the app.")
        return False
    if filled_code is not None:
        try:
            exec(filled_code)
            return True
        except:
            warnings.warn("chatgpt: execution failed, please make sure all credientials are correctly input in the yaml file.")
            return False
        