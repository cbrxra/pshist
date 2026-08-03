import argparse

from cli.commands.profile import init_profile_command

from cli.commands.config import init_config_command

from cli.commands.history import init_history_command

class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog = "pshist",
            description = "PowerShell History CLI",
        )

        self.parser.add_argument(
            "-v",
            "--version",
            action = "version",
            version = "%(prog)s 0.5"
        )

        self.subparsers = self.parser.add_subparsers(
            dest = "command",
            required = True
        )

        self._init_commands()

    def _init_commands(self):

        init_profile_command(self.subparsers)
        init_history_command(self.subparsers)
        init_config_command(self.subparsers)
        
    
    def get_parser(self):
        return self.parser.parse_args()