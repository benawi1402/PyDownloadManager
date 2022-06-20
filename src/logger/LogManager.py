import logging


class LogManager:
    def __init__(self):
        logging.basicConfig(filename='pydownloadmanager.log', encoding='utf-8', level=logging.DEBUG)
