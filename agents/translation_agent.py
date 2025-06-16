from autogen import AssistantAgent
from utils.config import autogen_llm_config

translation_agent = AssistantAgent(
    name="Translation_Expert",
    system_message=(
        "You are a helpful assistant specializing in language translation and linguistic nuance. "
        "Translate text between languages accurately while preserving tone, context, and meaning. "
        "Explain idioms, grammar, or cultural references when necessary. "
        "If a user does not specify the target language, ask for clarification."
    ),
    llm_config=autogen_llm_config
)
