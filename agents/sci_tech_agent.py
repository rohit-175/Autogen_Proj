from autogen import AssistantAgent
from utils.config import autogen_llm_config

science_agent = AssistantAgent(
    name="Science_Tech_Expert",
    system_message=(
        "You are a helpful assistant specializing in science and technology. "
        "Answer science and technology questions concisely, with key facts and clarity. " 
        "Avoid excessive detail unless specifically asked. Focus on the core answer. "
    ),
    llm_config=autogen_llm_config
)
