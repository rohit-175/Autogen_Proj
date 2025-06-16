from autogen import GroupChat, GroupChatManager
from agents.social_studies_agent import social_studies_agent
from agents.sci_tech_agent import science_agent
from agents.reviewer_agent import reviewer_agent
from agents.user_agent import user_proxy
from agents.math_agent import math_agent
from agents.literature_agent import english_lit_agent
from agents.translation_agent import translation_agent
from utils.config import autogen_llm_config

groupchat = GroupChat(
    agents=[user_proxy, social_studies_agent, science_agent, reviewer_agent, math_agent, english_lit_agent, translation_agent],
    messages=[],
    max_round=3
)

chat_manager = GroupChatManager(
    groupchat=groupchat,
    llm_config=autogen_llm_config
)
