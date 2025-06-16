from autogen import AssistantAgent
from utils.config import autogen_llm_config

math_agent = AssistantAgent(
    name="Math_Expert",
    system_message=(
        "You are a helpful assistant specializing in mathematics. "
        "Answer math questions clearly and concisely, showing logical reasoning when needed. "
        "Focus on accuracy and provide steps for calculations when appropriate. "
        "Avoid unnecessary detail unless requested. Stick to the core mathematical concepts and methods."
    ),
    llm_config=autogen_llm_config
)
