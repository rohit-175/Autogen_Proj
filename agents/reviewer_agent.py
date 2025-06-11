from autogen import AssistantAgent
from utils.config import autogen_llm_config

reviewer_agent = AssistantAgent(
    name="Reviewer",
    system_message=(
        "You are a critical reviewer. Your job is to evaluate the answers provided by other agents."
        "If the answer is factually correct and appropriate, reply with 'APPROVED'.\n"
        "If the answer is incorrect, unclear or off-topic, reply with 'REJECTED: wit a proper reason' "
        "Make sure to clearly state the reason when rejecting."
    ),
    llm_config=autogen_llm_config
)
