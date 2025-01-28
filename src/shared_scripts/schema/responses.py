from enum import Enum
from typing import Union

from pydantic import BaseModel, Field

from .llm import Anthropic_models, Google_models, Grok_models, Groq_models, LLMProvider, LLMTokenUsage, OpenaAI_models, Perplexity_models
from .primitives import ProcessingTimes, Video
from .tasks import TaskStatus


class WorkerExceptions(str, Enum):
    pass


class ProcessVideoExceptions(WorkerExceptions):
    InvalidURLException = "InvalidURLException"
    VideoProcessingException = "VideoProcessingException"
    VideoTranscriptionException = "VideoTranscriptionException"
    ProviderInvalidApiKeyException = "ProviderInvalidApiKeyException"
    ProviderModelException = "ProviderModelException"
    ProviderRateLimitExceededException = "ProviderRateLimitExceededException"
    ProviderTimeoutException = "ProviderTimeoutException"
    ProviderApiException = "ProviderApiException"


class VideoTaskResult(BaseModel):
    video_id: str
    message: str | None = None
    error_type: WorkerExceptions | None = None


class LLM(BaseModel):
    provider: LLMProvider
    model: Union[
        OpenaAI_models,
        Anthropic_models,
        Perplexity_models,
        Google_models,
        Groq_models,
        Grok_models,
    ]
    temperature: float
    max_tokens: int


class ProcessVideoResponse(VideoTaskResult):
    video: Video
    error_type: ProcessVideoExceptions | None = None
    llm: LLM
    processing_times: ProcessingTimes
    llm_token_usage: LLMTokenUsage


class TaskStatusResponse(BaseModel):
    video_id: str
    status: TaskStatus
    task_result: ProcessVideoResponse


class TaskResponse(BaseModel):
    message: str


class RecognizeTaskResponse(TaskResponse):
    video_id: str
