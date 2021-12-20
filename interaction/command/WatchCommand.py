from interaction.command.Command import Command


class WatchCommand(Command):
    def listen(self, commands):
        pass

    def get_command(self):
        return "watch"

    def get_args(self):
        return []

    def execute(self):
        print("Watch executed")
        pass
