"""
Main entry point for the TED-Ed AI Agent.
Coordinates the Ingestion Workflow and the Research Agent.
"""
import asyncio
from ingestion.workflow import TedEdIngestionWorkflow
from agent.agent import ask_agent
from temporalio.client import Client

async def run_full_pipeline(playlist_id: str):
    # 1. Connecting to Temporal
    client = await Client.connect("localhost:7233")
    
    # 2. Triggering Ingestion (Mock list for demo - in prod, use a scraper)
    videos = [
        {"id": "N1gaI3Qz6vw", "title": "Social Media & Sleep"},
        {"id": "example_id_2", "title": "The Science of Stress"}
    ]
    
    print(f"🚀 Starting ingestion for {len(videos)} videos...")
    await client.execute_workflow(
        TedEdIngestionWorkflow.run,
        videos,
        id=f"ingest-{playlist_id}",
        task_queue="ted-ed-queue"
    )

    # 3. Querying the Agent
    print("\n🤖 Agent is ready. Asking research question...")
    await ask_agent("Summarize the consensus on how screen time affects adolescent brain development.")

if __name__ == "__main__":
    asyncio.run(run_full_pipeline("PLJicmE8fK0EgB-UhtmREf-N1Z4Y_V6f5D"))
