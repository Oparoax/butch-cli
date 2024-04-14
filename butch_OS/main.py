import sys

from webbrowser import open as web_open
from random import choice as random_choice
from time import sleep

from module.file_importer import FileImporter
from module.progress import ProgressDisplay


class ConsoleHandler:
    def __init__(self):
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
        input_str = input()

        input_str.strip()
        keywords = input_str.split(" ")

        for keyword in keywords:
            keyword = keyword.lower()
            keyword = keyword.strip()

        match keywords[0]:
            case 'butch':
                self.butch_commands(keywords)
                return
            case 'kioshi':
                self.kioshi_commands(keywords)
            case 'help':
                return
            case 'exit':
                sys.exit()
            case _:
                print("Command not recognised")

    def butch_commands(self, commands):

        match commands[1]:
            case 'version':
                self.butch.get_version()
            case 'speak':
                print(f"butch says: {self.butch.get_butch_phrase()}")
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


class Butch:
    def __init__(self, phrases):
        self.phrases = phrases
        self.version = "0.9.2"

    def get_version(self):
        return print(f"Version: {self.version}")

    def get_butch_phrase(self):
        return random_choice(self.phrases['phrases'])


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

    print("----------------------------")
    print('= Welcome to butch-os v1.0 =')
    print("----------------------------")

    is_finished = False

    while not is_finished:
        console.listen_for_input()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
