from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from config.services import Services

class YoutubeClient(object):
    def __init__(self):
        self.DEVELOPER_KEY = Services.getYoutubeAPIToken()
        self.YOUTUBE_API_SERVICE_NAME = "youtube"
        self.YOUTUBE_API_VERSION = "v3"

    def search(self, criteria):
        youtube = self.initialiseLibrary()

        results = youtube.search().list(
            q=criteria,
            part="id,snippet",
            maxResults=10
        ).execute()

        for search_result in results.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                return search_result["id"]["videoId"]

    def initialiseLibrary(self):
        return build(
            self.YOUTUBE_API_SERVICE_NAME,
            self.YOUTUBE_API_VERSION,
            developerKey=self.DEVELOPER_KEY)

