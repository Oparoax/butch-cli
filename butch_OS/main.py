import sys
import pyttsx3

from webbrowser import open as web_open
from random import choice as random_choice
from time import sleep

from module.file_importer import FileImporter
from module.progress import ProgressDisplay


class ConsoleHandler:
    def __init__(self):
        self.phrase = None
        self.version = 1.0

        self.importer = FileImporter()
        self.progress_display = ProgressDisplay()

        self.butch_phrases = self.importer.phrases
        self.progress_msgs = self.importer.progress_msgs
        self.music_links = self.importer.links

        self.butch = Butch(self.butch_phrases)
        self.kioshi = Kioshi(self.music_links)

    def play_intro(self):
        self.progress_display.spinner('Welcome to ..', 2, "")

        print('\n')

        sleep(1)

        print(f"{self.importer.get_file_content('assets/title.txt')} \n")

        for msg in self.progress_msgs["progress_msgs"]:
            self.progress_display.loading_bar(msg['name'], msg['delay'], msg['complete'])

        sleep(2)

        print(self.importer.get_file_content('assets/butch-portrait.txt'))

        sleep(1)

        print(self.importer.get_file_content('assets/complete.txt'))

    def listen_for_input(self):
        input_str = input("<BUTCH-OS>:: ")

        filtered_keywords = self.filter_input(input_str)

        match filtered_keywords[0]:
            case 'version':
                print(f"v{self.version}")
            case 'butch':
                self.butch_commands(filtered_keywords)
                return
            case 'kioshi':
                self.kioshi_commands(filtered_keywords)
            case 'help':
                pass
            case 'exit':
                sys.exit()
            case _:
                pass

    def filter_input(self, input_str):
        # format inputs to be clear of whitespace
        input_str = input_str.strip()
        keywords = input_str.split(" ")

        filtered_keywords = []

        for keyword in keywords:
            word = keyword.strip()
            filtered_keywords.append(word.lower())

        return filtered_keywords

    def butch_commands(self, commands):

        match commands[1]:
            case 'version':
                self.butch.get_version()
            case 'speak':
                self.phrase = self.butch.get_butch_phrase()

                print(f"butch says: {self.phrase}")
                self.butch.speak(self.phrase)
            case 'say':
                print("What would you like butch to say?")
                self.phrase = input()
                self.butch.speak(self.phrase)
            case 'takeaway':
                print(
                    "Two Number 9's,"
                    "\n a number 9 large,"
                    "\n number 6 with extra dip,"
                    "\n number 7,"
                    "\n 2 number 45's, one with cheese,"
                    "\n and a large soda")
            case _:
                print("Command not recognised")

    def kioshi_commands(self, commands):

        match commands[1]:
            case 'version':
                self.kioshi.get_version()
            case 'play':
                self.kioshi.play_yt_playlist()
            case 'radio':
                self.kioshi.play_yt_radio()
            case _:
                print("Command not recognised")

    def print_welcome(self):
        welcome_string = f"= Welcome to butch-os v{self.version} ="
        string_len = len(welcome_string)

        print(string_len * "-")
        print(welcome_string)
        print(string_len * "-")


class Butch:
    def __init__(self, phrases):
        self.phrases = phrases
        self.version = "0.9.2"

        self.tts_engine = pyttsx3.init()

        # Default rate is much too high (200)
        self.tts_engine.setProperty('rate', 125)

    def get_version(self):
        return print(f"Version: {self.version}")

    def get_butch_phrase(self):
        return random_choice(self.phrases['phrases'])

    def speak(self, phrase):
        self.tts_engine.say(phrase)
        self.tts_engine.runAndWait()


class Kioshi:
    def __init__(self, links):
        self.links = links
        self.version = "v1.2.1"

    def get_version(self):
        return print(f"Version: {self.version}")

    def play_yt_playlist(self):
        self.play_yt(self.links['playlist'])

    def play_yt_radio(self):
        self.play_yt(self.links['radio'])

    def play_yt(self, link):
        print("Loading up ...")
        web_open(link[0])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    console = ConsoleHandler()
    debug_mode = False

    if len(sys.argv) > 1:
        if sys.argv[1] == "-d":
            debug_mode = True
    else:
        console.play_intro()

    console.print_welcome()

    is_finished = False

    while not is_finished:
        console.listen_for_input()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
