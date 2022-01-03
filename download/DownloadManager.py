from download.io.FileReceiver import FileReceiver
import asyncio


class DownloadManager:
    downloads = []
    queue = []
    default_memory_limit_per_download = 50

    def perform_download(self, download_info):
        fr = FileReceiver(download_info.url, download_info.file_path, download_info.limit, self.default_memory_limit_per_download)
        asyncio.run(fr.receive())

