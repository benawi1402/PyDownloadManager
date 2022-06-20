import requests, time
import asyncio
from download.io.algorithm.TokenBucket import TokenBucket
import logging


class FileReceiver:
    min_chunk_size = 1024
    max_chunk_size = 102400

    default_memory_limit_per_download = 50

    def __init__(self, download_info):
        """
        speed limit is given in Kb/1s

        TODO: parameter assertion
        """
        self.url = download_info.url
        self.speed_limit = download_info.limit
        self.memory_limit = self.default_memory_limit_per_download
        self.file_path = download_info.file_path

    async def receive(self):
        """
        TokenBucket dimensions: 1 token = 1 kilobit
        """
        session = requests.session()
        req = session.get(self.url, stream=True)
        req.raise_for_status()
        # per default we use 5 times the speed limit as token limit
        bucket = TokenBucket(self.speed_limit * 5, self.speed_limit)
        chunk_size = self.calculate_chunk_size()
        file = open(self.file_path, "wb")
        for data in req.iter_content(chunk_size=chunk_size):
            while not bucket.consume(chunk_size/1000):
                time.sleep(0.01)
            file.write(data)

        file.close()

    def calculate_chunk_size(self):
        chunk_size = self.speed_limit / 2
        return min(max(self.min_chunk_size, chunk_size), self.max_chunk_size)

    def run(self):
        asyncio.run(self.receive())