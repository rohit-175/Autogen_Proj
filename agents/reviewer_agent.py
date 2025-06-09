from autogen import AssistantAgent
from utils.config import autogen_llm_config

reviewer_agent = AssistantAgent(
    name="Reviewer",
    system_message="You are a strict reviewer. Evaluate answers for factual accuracy and conciseness. Only respond with 'APPROVED' if the answer is factually correct and to the point. Otherwise, respond with 'REJECTED: reason'.",
    llm_config=autogen_llm_config,
)
