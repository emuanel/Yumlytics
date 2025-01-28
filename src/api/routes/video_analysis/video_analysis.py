import time

from celery.utils import uuid
from celery_worker import worker
from fastapi import APIRouter, Form, Header, HTTPException, status
from fastapi.responses import JSONResponse

from config import settings
from schema.responses import RecognizeTaskResponse
from schema.llm import LLMProvider
from utils.utils import check_task_existance
from utils.logger import logger_video_analysis

router = APIRouter()


@router.post("/video_analysis", status_code=status.HTTP_202_ACCEPTED)
async def video_analysis(
    api_key: str = Header(default=None),
    provider: LLMProvider = Form(default=LLMProvider.OLLAMA),
    model: str = Form(default='deepseek-r1:8b'),
    video_data: str = Form(default='https://www.youtube.com/watch?v=ne7JIP4R5xM&t=93s'),
    temperature: float = Form(default=0.0),
    max_tokens: int = Form(default=1000)
) -> JSONResponse:
    """
    Endpoint to interact with multiple AI providers through a unified interface.
    It takes necessary parameters to generate a response from the selected AI provider.

    Parameters:
    - api_key (str): The API key for the selected provider, passed via request headers.
    - provider (str): The AI provider to use (Available: "ollama", "openai", "anthropic", "perplexity").
    - model (str): The specific model from the provider to use for generating responses.
    - data (str): JSON string containing ChatData information.
    - temperature (float, optional): The temperature setting for response generation. Defaults to 0.0.
    - max_tokens (int, optional): The maximum number of tokens in the response. Defaults to 1000.

    Returns:
    - dict: The response from the selected AI provider.
    """
    try:
        video_id: uuid = uuid().__str__()
        # Parse the JSON string back to ChatData
        logger_video_analysis.info(f"Video analysis: {provider} {model}, video: {video_data}")
        worker.send_task(
            "video_analysis",
            args=[provider, model, video_data, temperature, max_tokens, video_id],
            task_id=video_id,
        )

        max_wait_time = 20
        start_time = time.time()

        while time.time() - start_time < max_wait_time:
            if check_task_existance(video_id):
                logger_video_analysis.info(f"video_id: {video_id} Response: Document upload initiated and processing started")
                return RecognizeTaskResponse(
                    message="Document upload initiated and processing started",
                    video_id=video_id,
                )
            time.sleep(1)
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Document upload initiated but processing cant be started"
        )
    except Exception as e:
        logger_video_analysis.error(f"Internal server error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
