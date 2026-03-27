import os
from openai import OpenAI
from elasticsearch import Elasticsearch

class TedEdSemanticTools:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.es = Elasticsearch("http://localhost:9200")
        self.model = "text-embedding-3-small"

    def get_embedding(self, text: str):
        """Convert text into a 1536-dimension vector."""
        text = text.replace("\n", " ")
        return self.client.embeddings.create(input=[text], model=self.model).data[0].embedding

    def semantic_search(self, query: str) -> str:
        """Finds TED-Ed lessons based on meaning, not just keywords."""
        query_vector = self.get_embedding(query)

        # kNN (k-Nearest Neighbors) search in Elasticsearch
        search_query = {
            "field": "text_vector",
            "query_vector": query_vector,
            "k": 3,
            "num_candidates": 50
        }

        res = self.es.search(
            index="ted_ed_semantic",
            knn=search_query,
            source=["text", "title"]
        )

        results = []
        for hit in res['hits']['hits']:
            text_snippet = hit['_source']['text'][:800]
            results.append(f"Source: {hit['_source']['title']}\nContent: {text_snippet}...")
        
        return "\n\n---\n\n".join(results)
