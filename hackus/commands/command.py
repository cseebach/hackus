__author__ = 'Cameron Seebach'

import argparse
import StringIO


class MonkeyArgError(Exception):
    pass


class MonkeyArgParser(argparse.ArgumentParser):
    def _print_message(self, message, file=None):
        if not hasattr(self, "help_message"):
            self.help_message = StringIO.StringIO()
        self.help_message.write(message)

    def exit(self, status=0, message=None):
        self.help_message.write(message)
        self.help_message = self.help_message.getvalue()
        raise MonkeyArgError()


class Command(object):
    def run(self, shlex_args):
        try:
            args = self.parser.parse_args(shlex_args)
            return self.run_logic(args)
        except MonkeyArgError:
            return self.parser.help_message

