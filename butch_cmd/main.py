import json


def play_intro_sequence(self):


def load_json_phrases(self):
    phrases = json.load("butch-text.json")

    if not phrases is None:
        return phrases
    else:
        print("No phrases could be loaded for butch")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
