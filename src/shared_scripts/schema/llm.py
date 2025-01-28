from enum import Enum

from pydantic import BaseModel


class Ollama_models(str, Enum):
    # https://platform.openai.com/docs/models
    GPT_4O = "gpt-4o"
    CHATGPT_4O_LATEST = "chatgpt-4o-latest"
    GPT_4O_MINI = "gpt-4o-mini"
    GPT_4 = "gpt-4"
    GPT_4_TURBO = "gpt-4-turbo"
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_TURBO_16K = "gpt-3.5-turbo-16k"


class OpenaAI_models(str, Enum):
    # https://platform.openai.com/docs/models
    GPT_4O = "gpt-4o"
    CHATGPT_4O_LATEST = "chatgpt-4o-latest"
    GPT_4O_MINI = "gpt-4o-mini"
    GPT_4 = "gpt-4"
    GPT_4_TURBO = "gpt-4-turbo"
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_TURBO_16K = "gpt-3.5-turbo-16k"


class Anthropic_models(str, Enum):
    # https://docs.anthropic.com/en/docs/about-claude/models
    CLAUDE_3_5_SONNET_LATEST = "claude-3-5-sonnet-latest"
    CLAUDE_3_5_HAIKU_LATEST = "claude-3-5-haiku-latest"
    CLAUDE_3_OPUS_LATEST = "claude-3-opus-latest"
    CLAUDE_3_SONNET_20240229 = "claude-3-sonnet-20240229"
    CLAUDE_3_HAIKU_20240307 = "claude-3-haiku-20240307"


class Perplexity_models(str, Enum):
    # https://docs.perplexity.ai/guides/model-cards
    LLAMA_3_1_SONAR_LARGE_128K_ONLINE = "llama-3.1-sonar-large-128k-online"
    LLAMA_3_1_SONAR_SMALL_128K_ONLINE = "llama-3.1-sonar-small-128k-online"
    LLAMA_3_1_SONAR_HUGE_128K_ONLINE = "llama-3.1-sonar-huge-128k-online"


class Google_models(str, Enum):
    # https://ai.google.dev/gemini-api/docs/models/gemini
    GEMINI_1_5_PRO_LATEST = "gemini-1.5-pro-latest"
    GEMINI_1_5_PRO_001 = "gemini-1.5-pro-001"
    GEMINI_1_5_PRO_002 = "gemini-1.5-pro-002"
    GEMINI_1_5_FLASH_LATEST = "gemini-1.5-flash-latest"
    GEMINI_1_5_FLASH_001 = "gemini-1.5-flash-001"
    GEMINI_1_5_FLASH_001_TUNING = "gemini-1.5-flash-001-tuning"
    GEMINI_1_5_FLASH = "gemini-1.5-flash"
    GEMINI_1_5_FLASH_002 = "gemini-1.5-flash-002"
    GEMINI_1_5_FLASH_8B = "gemini-1.5-flash-8b"
    GEMINI_1_5_FLASH_8B_001 = "gemini-1.5-flash-8b-001"
    GEMINI_1_5_FLASH_8B_LATEST = "gemini-1.5-flash-8b-latest"


class Groq_models(str, Enum):
    # https://console.groq.com/docs/models
    GEMMA2_9B_IT = "gemma2-9b-it"
    LLAMA3_70B_8192 = "llama3-70b-8192"
    LLAMA3_8B_8192 = "llama3-8b-8192"
    LLAMA_3_1_70B_VERSATILE = "llama-3.1-70b-versatile"
    LLAMA_GUARD_3_8B = "llama-guard-3-8b"
    MIXTRAL_8X7B_32768 = "mixtral-8x7b-32768"
    LLAMA_3_1_8B_INSTANT = "llama-3.1-8b-instant"
    LLAMA_3_3_70B_VERSATILE = "llama-3.3-70b-versatile"


class Grok_models(str, Enum):
    # https://docs.x.ai/docs/models
    GROK_2_1212 = "grok-2-1212"
    GROK_BETA = "grok-beta"


class LLMProvider(str, Enum):
    OLLAMA = "ollama"
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GOOGLE = "google"
    XAI = "xai"
    GROQ = "groq"
    PERPLEXITY = "perplexity"


class LLMTokenUsage(BaseModel):
    input_tokens: float
    output_tokens: float
    total_tokens: float
    cost: float