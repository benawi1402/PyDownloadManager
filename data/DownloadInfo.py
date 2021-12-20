import validators

from exception.DownloadURLException import DownloadURLException


class DownloadInfo:
    """Class containing all infos for a download"""

    def __init__(self, url, limit, name="", priority=0):
        if not validators.url(url):
            raise DownloadURLException(url, "URL could not be validated!")
        self.limit = limit
        self.url = url
        self.priority = priority
        self.name = name
