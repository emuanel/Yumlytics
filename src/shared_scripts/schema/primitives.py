from datetime import datetime
from enum import Enum

from pydantic import BaseModel

from .transcription import ValidLanguages


class ProcessingTimes(BaseModel):
    transcription: float
    text_analysis: float
    total: float


class VideoData(BaseModel):
    url: str
    lenght: int
    title: str
    description: str
    language: ValidLanguages
    publishing_date: datetime
    view_count: int
    like_count: int
    dislike_count: int


class Reviewer(BaseModel):
    name: str
    email: str | None


class Opinion(str, Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"


class OpinionData(BaseModel):
    opinion: Opinion
    confidence: float


class Video(BaseModel):
    data: VideoData
    reviewer: Reviewer
    opinion: OpinionData
