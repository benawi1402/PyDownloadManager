from .Command import Command


class LsCommand(Command):
    def get_command(self):
        return "ls"

    def get_args(self):
        return []

    def execute(self):
        print("Ls executed")
        pass
