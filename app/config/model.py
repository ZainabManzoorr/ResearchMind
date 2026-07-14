from smolagents import LiteLLMModel

from app.config.settings import GROQ_API_KEY

model = LiteLLMModel(
  model_id="groq/llama-3.3-70b-versatile",
  api_key=GROQ_API_KEY
)