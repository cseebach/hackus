__author__ = 'Cameron Seebach'

from hackus.commands.command import Command, MonkeyArgParser


class Logout(Command):
    name = "logout"

    def __init__(self):
        self.parser = MonkeyArgParser(prog=self.name, description="log out of the system")

    def run_logic(self, args):
        self.system.logout()
        self.system.clear_commands()
        self.system.add_command(Login)
        return "you are now logged out.\nCOMMANDS AVAILABLE: login\n"


class Login(Command):
    name = "login"

    def __init__(self):
        self.parser = MonkeyArgParser(prog=self.name, description="login to the system")
        self.parser.add_argument("username")
        self.parser.add_argument("password")

    def run_logic(self, args):
        if args.username == "admin" and args.password == "password":
            self.system.login("admin")
            self.system.remove_command(Login)
            self.system.add_command(Logout)
            return ""
        else:
            return "incorrect username or password"
        
