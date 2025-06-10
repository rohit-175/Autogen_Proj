from autogen import AssistantAgent
from utils.config import autogen_llm_config

social_studies_agent = AssistantAgent(
    name="SST_Expert",
    system_message=(
        "You are a Social Studies Expert specializing in History, Geography, Civics, and Economics.  "
        "Answer science and technology questions concisely, with key facts and clarity. " 
        "Avoid excessive detail unless specifically asked. Focus on the core answer. "
    ),
    llm_config=autogen_llm_config,
)
