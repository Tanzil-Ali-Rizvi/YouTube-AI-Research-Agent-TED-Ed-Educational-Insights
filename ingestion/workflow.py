from datetime import timedelta
from temporalio import workflow
with workflow.unsafe.imports_passed_through():
    from ingestion.activities import YoutubeActivities

@workflow.defn
class TedEdIngestionWorkflow:
    @workflow.run
    async def run(self, playlist_videos: list):
        for video in playlist_videos:
            transcript = await workflow.execute_activity(
                YoutubeActivities.fetch_transcript,
                video['id'],
                start_to_close_timeout=timedelta(minutes=2)
            )
            await workflow.execute_activity(
                YoutubeActivities.index_document,
                {"video_id": video['id'], "title": video['title'], "text": transcript},
                start_to_close_timeout=timedelta(seconds=30)
            )
