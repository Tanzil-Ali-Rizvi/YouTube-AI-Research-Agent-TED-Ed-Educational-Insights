import os
from temporalio import activity
from youtube_transcript_api import YouTubeTranscriptApi
from elasticsearch import Elasticsearch

class YoutubeActivities:
    def __init__(self, es_client: Elasticsearch):
        self.es = es_client

    @activity.def
    async def fetch_transcript(self, video_id: str) -> str:
        # Configurating for Proxy (essential for TED-Ed bulk scraping)
        proxy = {
            "http": f"http://{os.getenv('PROXY_USER')}:{os.getenv('PROXY_PASSWORD')}@{os.getenv('PROXY_BASE_URL')}",
            "https": f"http://{os.getenv('PROXY_USER')}:{os.getenv('PROXY_PASSWORD')}@{os.getenv('PROXY_BASE_URL')}"
        }
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, proxies=proxy)
        return " ".join([t['text'] for t in transcript_list])

    @activity.def
    async def index_document(self, data: dict):
        self.es.index(index="ted_ed_content", id=data['video_id'], document=data)
