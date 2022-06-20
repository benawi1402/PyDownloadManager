from .Command import Command


class QueueCommand(Command):
    def get_command(self):
        return "queue"

    def get_args(self):
        return []

    def execute(self):
        pass
