import yaml
import argparse
from bot import ChatbotWrapper
import warnings
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--yaml")
    args = parser.parse_args()
    return args

def load_yaml(path):
    with open(path, 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials

def main():
    args = get_args()
    credentials = load_yaml(args.yaml)
    # start connection with openAI chatgpt, once official API is here, should be replaced.
    try:
        bot = ChatbotWrapper(credentials)
    except Exception as exc:
            print(f"Error: {exc}")
            assert False

    print("Starting conversation, please type in your commands:")
    while True:
        prompt = input("Me:")
        if prompt == "exit":
            print("your conversation with chatgpt has ended.")
            break
        elif prompt == "run it":
            bot.parse_and_execute()
        else:
            app = bot.parse_app_name_updated(prompt)
            response = bot.get_chat_response(prompt, app)
            if response['message'] is None:
                warnings.warn(f"Error: {response['message']}")
            else:
                print(f"chatgpt: {response['message']}")
if __name__ == "__main__":
    main()