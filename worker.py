import asyncio
from temporalio.client import Client
from temporalio.worker import Worker
from elasticsearch import Elasticsearch
from ingestion.activities import YoutubeActivities
from ingestion.workflow import TedEdIngestionWorkflow

async def main():
    client = await Client.connect("localhost:7233")
    es = Elasticsearch("http://localhost:9200")
    activities = YoutubeActivities(es)
    
    worker = Worker(
        client,
        task_queue="ted-ed-queue",
        workflows=[TedEdIngestionWorkflow],
        activities=[activities.fetch_transcript, activities.index_document],
    )
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
