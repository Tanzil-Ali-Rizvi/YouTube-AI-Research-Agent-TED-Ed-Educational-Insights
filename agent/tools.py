from elasticsearch import Elasticsearch

class TedEdTools:
    def __init__(self):
        self.es = Elasticsearch("http://localhost:9200")

    def search_lessons(self, query: str) -> str:
        """Search the TED-Ed 'Are the kids alright?' lessons for specific topics."""
        res = self.es.search(
            index="ted_ed_content",
            query={"match": {"text": query}}
        )
        return "\n".join([hit['_source']['text'][:1000] for hit in res['hits']['hits']])
