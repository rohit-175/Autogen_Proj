from agents.user_agent import user_proxy
from manager.chat_manager import chat_manager

user_query = input("Enter your question: ")

user_proxy.initiate_chat(
    chat_manager,
    message=user_query
)
