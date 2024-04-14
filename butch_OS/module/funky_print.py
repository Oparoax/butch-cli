

class FunkyPrint:

    def pr_status_msg(self, result):
        if result:
            self.pr_green('Complete')
        else:
            self.pr_red('Failed')

    def pr_red(self, txt):
        print("\033[91m {}\033[00m".format(txt))

    def pr_green(self, txt):
        print("\033[92m {}\033[00m".format(txt))