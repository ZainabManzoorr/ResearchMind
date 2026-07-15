from smolagents import tool

from app.embeddings.embedder import Embedder
from app.vectorstore.chroma_store import ChromaStore

embedder = Embedder()
store = ChromaStore()

@tool

def retrieval_tool(query: str) -> str:
    """
    Retrieve relevant information from the user's private AI research notes.

    Use this tool whenever the user asks about:
    - personal research notes
    - RAG concepts from notes
    - AI engineering topics stored in knowledge base

    Args:
        query: Topic to search.

    Returns:
        Relevant content from the user's notes.
    """

    embedding = embedder.embed(query)

    results = store.search(embedding)

    if results and results['documents']:
        return results['documents'][0][0]

    return "No relevant information found."