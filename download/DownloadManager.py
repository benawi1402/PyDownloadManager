from download.io.FileReceiver import FileReceiver
import asyncio


class DownloadManager:
    downloads = []
    queue = []


    def perform_download(self, download_info):
        fr = FileReceiver(download_info.url, download_info.file_path, download_info.limit, self.default_memory_limit_per_download)
        fr.run()
