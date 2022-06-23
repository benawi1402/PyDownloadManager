import validators

from exception.DownloadURLError import DownloadURLException


class DownloadInfo:
    limit = -1
    url = ""
    priority = 1
    name = ""
    file_path = ""
    """Class containing all infos for a download"""

    def __init__(self, url, limit, file_path, name="", priority=0):
        if not validators.url(url):
            raise DownloadURLException(url, "URL could not be validated!")
        self.limit = limit
        self.url = url
        self.priority = priority
        self.name = name
        self.file_path = file_path
