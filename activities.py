@activity.def
async def index_semantic_document(self, data: dict):
    # Initializing the tools class to use the embedding logic
    tools = TedEdSemanticTools() 
    
    # Generating the vector for the transcript
    vector = tools.get_embedding(data['text'])
    
    # Indexing both the text and the vector
    document = {
        "video_id": data['video_id'],
        "title": data['title'],
        "text": data['text'],
        "text_vector": vector  # This is the 'semantic' heart of the project
    }
    
    self.es.index(index="ted_ed_semantic", id=data['video_id'], document=document)
