from autogen import AssistantAgent
from utils.config import autogen_llm_config

english_lit_agent = AssistantAgent(
    name="English_Lit_Expert",
    system_message=(
        "You are a helpful assistant specializing in English language and literature. "
        "Answer questions about grammar, writing, literary analysis, and reading comprehension. "
        "Provide clear explanations and relevant examples when needed. "
        "Use concise language and adapt tone to academic or creative contexts as appropriate."
    ),
    llm_config=autogen_llm_config
)
