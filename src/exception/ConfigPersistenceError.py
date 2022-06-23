class ConfigPersistenceError(Exception):
    def __init__(self, msg, attached_exception=None):
        self.attached_exception = attached_exception
        self.message = msg
