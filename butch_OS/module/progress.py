from random import choice as random_choice
from time import sleep, time

from progress.bar import ShadyBar
from progress.spinner import Spinner
from funky_print import FunkyPrint


class ProgressDisplay:
    def __init__(self):
        self.bar_max = 100
        self.funk_print = FunkyPrint()

    def loading_bar(self, process_name, delay, is_completed=True):
        if is_completed:
            bar_max = self.bar_max
        else:
            bar_max = self.bar_max - random_choice([20, 15, 10, 5])

        if delay > 0.2:
            self.funk_print.pr_red("WTF that delay is too long")
            return

        with ShadyBar(process_name, max=self.bar_max) as bar:
            for i in range(bar_max):
                # Do some work
                sleep(delay)
                bar.next()
            bar.finish()
            self.funk_print.pr_status_msg(is_completed)

    def spinner(self, process_name, delay, complete_msg):
        spinner = Spinner(process_name)
        time_elapsed = 0

        start = time()

        if delay > 5:
            self.funk_print.pr_red("WTF that delay is too long")
            return

        while time_elapsed < delay:
            time_elapsed = time() - start
            spinner.next()

        spinner.finish()

        if complete_msg is not None:
            print(complete_msg)
