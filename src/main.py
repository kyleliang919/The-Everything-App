import yaml
import argparse
from revChatGPT.revChatGPT import Chatbot
from apps import parse_and_execute, detect_code
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
        bot = Chatbot(config=credentials["chatgpt"], debug=True)
        bot.refresh_session()
    except Exception as exc:
            print(f"Error: {exc}")
            assert False

    print("Starting conversation, please type in your commands:")
    while True:
        prompt = input("Me:")
        if prompt == "exit":
            print("your conversation with chatgpt has ended.")
            break
        else:
            response = bot.get_chat_response(prompt)
            if response['message'] is None:
                print("Error: response['message'] is None")
                assert False
            else:
                code_gen = detect_code(response['message'])
                if code_gen is not None:
                    execute_or_not = input("chatgpt: code generation detected, do you want to execute?")
                    if execute_or_not == "yes":
                        parse_and_execute(code_gen, credentials, bot)
                    else:
                        print(f"chatgpt: no code has been executed.")
                else:
                    print(f"chatgpt: {response['message']}")

        # parse the response
if __name__ == "__main__":
    main()