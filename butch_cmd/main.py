import datetime
import json
import random
import time

from progress.bar import Bar, ShadyBar
from progress.spinner import Spinner


class ConsoleHandler:
    def __init__(self):
        self.importer = FileImporter()
        self.progress_display = ProgressDisplay()

        self.butch_phrases = self.importer.phrases
        self.progress_msgs = self.importer.progress_msgs

        self.butch_phrases = ButchPhrases(self.butch_phrases)

    def play_intro(self):
        print("Welcome to....")
        time.sleep(0.5)
        print(self.importer.get_file_content('Assets/title.txt'))

        self.progress_display.loading_bar("Arms", 0.2, "Complete: Arm's locked and loaded")


class ButchPhrases:
    def __init__(self, phrases):
        self.phrases = phrases

    def play_butch_phrase(self):
        print(random.choice(self.phrases))


class ProgressDisplay:
    def __init__(self):
        self.bar_max = 100

    def loading_bar(self, process_name, delay, complete_msg):
        if delay > 0.2:
            print("WTF that delay is too long")
            return

        with Bar(process_name, max=self.bar_max) as bar:
            for i in range(self.bar_max):
                # Do some work
                time.sleep(delay)
                bar.next()
            bar.finish()

        print(complete_msg)

    def spinner(self, process_name, delay, complete_msg):
        spinner = Spinner(process_name)
        time_elapsed = 0

        if delay > 100:
            print("WTF that delay is too long")
            return

        while time_elapsed < delay:
            time_elapsed += datetime.timedelta
            spinner.next()


class FileImporter:
    def __init__(self):
        self.phrases = self.load_json_phrases()
        self.progress_msgs = self.load_json_intro_progress()

    def get_file_content(self, filepath):
        text_file = open(filepath, 'r')
        text = text_file.read()
        text_file.close()

        if text is not None:
            return text
        else:
            print(f"File not found: {filepath}")

    def get_json_content(self, filepath):
        text_file = open(filepath, 'r')
        text = json.load(text_file)

        return text

    def load_json_phrases(self):
        phrases = self.get_json_content('Assets/butch_text.json')

        if phrases is not None:
            return phrases
        else:
            print('No phrases could be loaded for butch')

    def load_json_intro_progress(self):
        progress_msgs = self.get_json_content('Assets/butch_progress.json')

        if progress_msgs is not None:
            return progress_msgs
        else:
            print('No progress msgs could be loaded for butch')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    console = ConsoleHandler()
    console.play_intro()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
