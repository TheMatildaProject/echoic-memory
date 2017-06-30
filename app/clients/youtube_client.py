from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

class YoutubeClient(object):
    def __init__(self):
        self.DEVELOPER_KEY = ""
        self.YOUTUBE_API_SERVICE_NAME = "youtube"
        self.YOUTUBE_API_VERSION = "v3"

    def search(self):
        youtube = self.initialiseLibrary()

        print(search_response = youtube.search().list(
            q="Ŝystem of a Down",
            part="id,snippet",
            maxResults=options.max_results
        ).execute())

    def initialiseLibrary(self):
        return build(
            self.YOUTUBE_API_SERVICE_NAME,
            self.YOUTUBE_API_VERSION,
            developerKey=self.DEVELOPER_KEY)

