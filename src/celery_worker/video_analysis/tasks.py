from datetime import datetime
from celery_app import celery_app
from fastapi.encoders import jsonable_encoder

from config import settings
from schema.llm import LLMTokenUsage
from schema.responses import LLM, ProcessVideoExceptions, ProcessVideoResponse
from schema.primitives import OpinionData, ProcessingTimes, Reviewer, Video, VideoData
from utils import logger_celery

MOCK_SCHEMA = ProcessVideoResponse(
    video_id="test",
    message="test",
    video=Video(
        data=VideoData(
            url="https://www.youtube.com/watch?v=test",
            lenght=0,
            title="Test video",
            description="Test description",
            language="pl",
            publishing_date=datetime.now(),
            view_count=0,
            like_count=0,
            dislike_count=0

        ),
        reviewer=Reviewer(
            name="Test reviewer",
            email="",
        ),
        opinion=OpinionData(
            opinion="neutral",
            confidence=0.0
        )
    ),
    processing_times=ProcessingTimes(
        transcription=0,
        text_analysis=0,
        total=0
    ),
    llm_token_usage=LLMTokenUsage(
        input_tokens=0,
        output_tokens=0,
        total_tokens=0,
        cost=0
    ),
    llm=LLM(
        provider="openai",
        model="gpt-3.5-turbo",
        temperature=0,
        max_tokens=100
    )
)


@celery_app.task(name="video_analysis", bind=True, task_time_limit=4, soft_time_limit=4, default_retry_delay=5, max_retries=2)
def process_video(self, provider: str, model: str, video_link: str, temperature: float, max_tokens: int, video_id: str) -> ProcessVideoResponse:
    logger_celery.info(f"Processing video with ID: {video_id} and yt link: {video_link}")
    if settings.return_mock_parsed_schema:
        get_content_result = MOCK_SCHEMA
        return jsonable_encoder(get_content_result)

    try:
        # analyze_video(provider, model, video_link, temperature, max_tokens, video_id)
        return jsonable_encoder(get_content_result)
    except Exception as e:
        logger_celery.error(f"Exception: {str(e)}")
        process_result = ProcessVideoResponse(
            error_type=ProcessVideoExceptions(type(e).__name__),
            message=str(e),
            document_id=video_id,
        )
        return jsonable_encoder(process_result)
