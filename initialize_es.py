from elasticsearch import Elasticsearch
import os
from dotenv import load_dotenv

load_dotenv()

def initialize_index():
    es = Elasticsearch(os.getenv("ELASTICSEARCH_URL", "http://localhost:9200"))
    
    index_name = "ted_ed_semantic"

    # Defining the mapping
    # Used 1536 dimensions to match OpenAI's 'text-embedding-3-small'
    mappings = {
        "properties": {
            "video_id": {"type": "keyword"},
            "title": {"type": "text"},
            "text": {"type": "text"},
            "text_vector": {
                "type": "dense_vector",
                "dims": 1536,
                "index": True,
                "similarity": "cosine"  # Best for comparing text meanings
            }
        }
    }

    if es.indices.exists(index=index_name):
        print(f"Index {index_name} already exists. Recreating...")
        es.indices.delete(index=index_name)

    # Create the index
    es.indices.create(index=index_name, mappings=mappings)
    print(f"✅ Successfully initialized {index_name} with Vector Search capabilities.")

if __name__ == "__main__":
    initialize_index()
