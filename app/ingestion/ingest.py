from app.ingestion.loader import DocumentLoader
from app.embeddings.embedder import Embedder
from app.vectorstore.chroma_store import ChromaStore


loader = DocumentLoader()

embedder = Embedder()

store = ChromaStore()


document = loader.load(
    "app/knowledge/ai_notes.txt"
)

embedding = embedder.embed(document)

store.add(
    documents=[document],
    embeddings=[embedding]
)

print("Knowledge Base Created")