from autogen import AssistantAgent
from utils.config import autogen_llm_config

history_agent = AssistantAgent(
    name="History_Prof",
    system_message="You are a History Professor. Answer historical questions concisely, with key facts and clarity, avoiding excessive detail unless specifically asked. Focus on the core answer.",
    llm_config=autogen_llm_config,
)
