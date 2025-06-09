from autogen import GroupChat, GroupChatManager
from agents.history_agent import history_agent
from agents.reviewer_agent import reviewer_agent
from agents.user_agent import user_proxy
from utils.config import autogen_llm_config

groupchat = GroupChat(
    agents=[user_proxy, history_agent, reviewer_agent],
    messages=[],
    max_round=3
)

chat_manager = GroupChatManager(
    groupchat=groupchat,
    llm_config=autogen_llm_config
)
