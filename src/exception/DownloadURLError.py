class DownloadURLException(Exception):
    def __init__(self, url, msg):
        self.url = url
        self.message = msg
