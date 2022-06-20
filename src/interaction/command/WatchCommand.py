from .Command import Command


class WatchCommand(Command):
    def get_command(self):
        return "watch"

    def get_args(self):
        return []

    def execute(self):
        print("Watch executed")
        pass
