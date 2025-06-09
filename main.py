from agents.user_agent import user_proxy
from manager.chat_manager import chat_manager

user_proxy.initiate_chat(
    chat_manager,
    message="Who was the first emperor of the Mughal Empire?"
)
