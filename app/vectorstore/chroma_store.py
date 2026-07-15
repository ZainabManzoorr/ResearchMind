import chromadb

class ChromaStore:
  
    def __init__(self):
      self.client = chromadb.Client()
      
      self.collection = (self.client.get_or_create_collection("research_notes"))
    def add(
      self,
      documents,
      embeddings,
    ):
      self.collection.add(
        documents=documents,
        embeddings=embeddings,
        ids =[
          str(i)
          for i in range(len(documents))
        ]
      )
    def search(
      self,
      embedding,
    
    ):
      return self.collection.query(
        query_embeddings=[embedding],
        n_results=2
      )
      