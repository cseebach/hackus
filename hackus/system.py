from hackus.commands.users import Login

__author__ = 'Cameron Seebach'

import shlex


class System(object):
    def __init__(self, console):
        self.commands = {}
        self.console = console
        self.console.set_system(self)

    def boot(self):
        self.add_command(Login)

        self.console.set_prompt("> ")

        self.console.write("booting chaOS v1.22\nWelcome. Please login.\nCOMMANDS AVAILABLE: login\n")
        self.console.set_input()

    def login(self, username):
        self.console.set_prompt("{}@pc06:~> ".format(username))

    def logout(self):
        self.console.set_prompt("> ")

    def add_command(self, command_class):
        self.commands[command_class.name] = command_class

    def remove_command(self, command_class):
        del self.commands[command_class.name]

    def clear_commands(self):
        self.commands.clear()

    def evaluate_command(self, command):
        shlex_args = shlex.split(command)
        if shlex_args[0] in self.commands:
            command_instance = self.commands[shlex_args[0]]()
            command_instance.system = self
            self.console.write(command_instance.run(shlex_args[1:]))
            self.console.set_input()
        else:
            self.console.write("no such command: '{}'\n".format(shlex_args[0]))
            self.console.set_input()
