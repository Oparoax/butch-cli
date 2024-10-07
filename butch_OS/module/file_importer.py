from json import load as js_load
import os

CURR_DIR = os.path.dirname(__file__) + '/..'

class FileImporter:
    def __init__(self):
        self.phrases = self.load_json_phrases()
        self.progress_msgs = self.load_json_intro_progress()
        self.links = self.load_json_kioshi_links()

    def get_file_content(self, filepath):
        text_file = open(CURR_DIR + '/' + filepath, 'r')
        text = text_file.read()
        text_file.close()

        if text is not None:
            return text
        else:
            print(f"File not found: {filepath}")

    def get_json_content(self, filepath):
        text_file = open(CURR_DIR + '/' + filepath, 'r')
        text = js_load(text_file)

        return text

    def load_json_phrases(self):
        phrases = self.get_json_content('json/butch_text.json')

        if phrases is not None:
            return phrases
        else:
            print('No phrases could be loaded for butch')

    def load_json_intro_progress(self):
        progress_msgs = self.get_json_content('json/butch_loading_text.json')

        if progress_msgs is not None:
            return progress_msgs
        else:
            print('No progress msgs could be loaded for butch')

    def load_json_kioshi_links(self):
        links = self.get_json_content('json/kioshi_links.json')

        if links is not None:
            return links
        else:
            print('No links could be loaded for kioshi')
