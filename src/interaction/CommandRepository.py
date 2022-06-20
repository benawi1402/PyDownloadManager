import os
import inspect
import importlib

from interaction.command.Command import Command


class CommandRepository:
    commands_imported = False
    commands = {}

    def import_commands(self):
        """
        Get all command modules and import them, then return a dir with every command object and command string.
        Importing modules a second time is impossible
        """
        if not self.commands_imported:
            current_file_path = os.path.dirname(inspect.stack()[0][1])
            for file in [f for f in os.listdir(os.path.join(current_file_path, 'command')) if f.endswith('.py') and f not in ['__init__.py', 'Command.py']]:
                module_name = file.removesuffix('.py')
                importlib.import_module(f'.{module_name}', 'interaction.command')
            self.commands_imported = True

    def find_commands(self):
        self.import_commands()
        if self.commands != {}:
            return self.commands
        for command in Command.__subclasses__():
            new_command = command()
            self.commands[new_command.get_command()] = new_command
        return self.commands
