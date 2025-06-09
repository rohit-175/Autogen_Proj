import os
from dotenv import load_dotenv

load_dotenv()

azure_openai_config_list = [
    {
        "model": os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
        "base_url": os.getenv("AZURE_OPENAI_API_BASE"),
        "api_type": "azure",
        "api_version": os.getenv("AZURE_OPENAI_API_VERSION"),
    }
]
autogen_llm_config = {
    "config_list": azure_openai_config_list,
    "cache_seed": 42,
}
