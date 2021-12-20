from interaction.command.Command import Command


class LsCommand(Command):
    def listen(self, commands):
        pass

    def get_command(self):
        return "ls"

    def get_args(self):
        return []

    def execute(self):
        print("Ls executed")
        pass
