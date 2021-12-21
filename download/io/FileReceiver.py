import requests, time

class FileReceiver:
    def __init__(self, url, speed_limit):
        self.url = url
        self.speed_limit = speed_limit

    async def receive(self):
        