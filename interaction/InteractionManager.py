from interaction.CommandRepository import CommandRepository
from interaction.command.Command import Command
import argparse


class InteractionManager:
    command_repo = CommandRepository()

    def get_argument_parser(self):
        parser = argparse.ArgumentParser(description='PyDownloadManager, created by Frederik Maassen. Simple and clean python download manager that lives in your console/terminal/bash.')
        str_commands = []
        command_dict = self.command_repo.find_commands()
        for key in command_dict:
            str_commands.append(key)
        parser.add_argument('command', choices=str_commands, help='Calls one of the defined commands')
        return parser

    def parse_args(self):
        parser = self.get_argument_parser()
        args = parser.parse_args()
        self.command_repo.find_commands()[args.command].execute()

