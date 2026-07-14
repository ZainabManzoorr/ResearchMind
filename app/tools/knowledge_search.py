from smolagents import tool


@tool
def knowledge_search(query: str) -> str:
    """
    Search the user's private AI research notes.

    Use this tool whenever the user asks about:
    - personal research notes
    - RAG concepts from notes
    - AI engineering topics stored in knowledge base

    Args:
        query: Topic to search.

    Returns:
        Relevant content from the user's notes.
    """

    with open(
        "app/knowledge/ai_notes.txt",
        "r"
    ) as file:

        knowledge = file.read()


    if query.lower() in knowledge.lower():
        return knowledge

    return "No relevant information found."