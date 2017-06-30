import os

class Services():
    @staticmethod
    def getYoutubeAPIToken():
        return os.getenv('YOUTUBE_API_TOKEN')