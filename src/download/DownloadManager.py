from io.FileReceiver import FileReceiver


class DownloadManager:
    downloads = []
    queue = []

    def perform_download(self, download_info):
        fr = FileReceiver(download_info)
        fr.run()
