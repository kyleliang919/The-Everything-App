import yaml
import argparse
from bot import Chatbot
from controller import parse_and_execute
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
        bot = Chatbot()
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
                code_gen = response['code_gen']
                if code_gen is not None:
                    execute_or_not = input("chatgpt: code generation detected, do you want to execute?(yes/no)")
                    if execute_or_not == "yes":
                        success = parse_and_execute(code_gen, credentials, bot)
                        if success:
                            print(f"chatgpt: execution succeeded, please check the app for results")
                        else:
                            print(f"chatgpt: execution failed, please try a different prompt") 
                    else:
                        print(f"chatgpt: no code has been executed, continue on the coversation.")
                else:
                    print(f"chatgpt: {response['message']}")

        # parse the response
if __name__ == "__main__":
    main()