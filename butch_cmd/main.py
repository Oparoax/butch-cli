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

        self.butch_phrases = Butch(self.butch_phrases)

    def play_intro(self):
        self.progress_display.spinner('Welcome to...', 3, '')
        time.sleep(0.5)
        print(f"{self.importer.get_file_content('Assets/title.txt')} \n")

        for msg in self.progress_msgs["progress_msgs"]:
            self.progress_display.loading_bar(msg['name'], msg['delay'], msg['complete'])

        print(self.importer.get_file_content('Assets/complete.txt'))

        time.sleep(1)

        print(self.importer.get_file_content('Assets/butchportrait.txt'))


class Butch:
    def __init__(self, phrases):
        self.phrases = phrases

    def play_butch_phrase(self):
        print(random.choice(self.phrases))


class ProgressDisplay:
    def __init__(self):
        self.bar_max = 100
        self.funk_print = FunkyPrint()

    def loading_bar(self, process_name, delay, is_completed=True):
        if is_completed:
            bar_max = self.bar_max
            success_msg = 'Completed'
        else:
            bar_max = self.bar_max - 20
            success_msg = 'Failed'

        if delay > 0.2:
            self.funk_print.pr_red("WTF that delay is too long")
            return

        with Bar(process_name, max=self.bar_max) as bar:
            for i in range(bar_max):
                # Do some work
                time.sleep(delay)
                bar.next()
            bar.finish()
            self.funk_print.pr_result(is_completed)

    def spinner(self, process_name, delay, complete_msg):
        spinner = Spinner(process_name)
        time_elapsed = 0

        if delay > 30:
            self.funk_print.pr_red("WTF that delay is too long")
            return

        while time_elapsed < delay:
            time_elapsed += 
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
        progress_msgs = self.get_json_content('Assets/butch_loading_text.json')

        if progress_msgs is not None:
            return progress_msgs
        else:
            print('No progress msgs could be loaded for butch')


class FunkyPrint:

    def pr_result(self, result):
        if result:
            self.pr_green('Complete')
        else:
            self.pr_red('Failed')

    def pr_red(self, txt):
        print("\033[91m {}\033[00m".format(txt))

    def pr_green(self, txt):
        print("\033[92m {}\033[00m".format(txt))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    console = ConsoleHandler()
    console.play_intro()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
