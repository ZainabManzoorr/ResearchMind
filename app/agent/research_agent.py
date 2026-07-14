from smolagents import CodeAgent
from app.config.model import model
from app.tools.knowledge_search import knowledge_search
agent = CodeAgent(
  model = model,
  tools =[
    knowledge_search
  ],
  instructions = """You are ResearchMind.

    You are an AI research assistant
    specialized in:

  Rules:
    1. Use search_knowledge when answering
       questions related to stored research notes.
    2. Prefer user knowledge over general knowledge.
    3. Explain concepts technically but clearly.
    """
  
)

