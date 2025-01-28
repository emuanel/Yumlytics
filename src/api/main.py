import logging
import os

import uvicorn
from config import settings
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import health_router, video_analysis_router

logging.basicConfig(
    level=settings.logging.parsed_log_level,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler(os.path.join(settings.logging.log_dir, "main.log"))
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter(
    "%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
))

logger.addHandler(file_handler)

app = FastAPI(title=settings.app_name)

logger.info(f"Configuring CORS with origins: {settings.origins}")
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
logger.info("CORS middleware configured successfully")

api_router = APIRouter()

api_router.include_router(health_router, prefix="/health", tags=["health"])
api_router.include_router(video_analysis_router, prefix="/video_analysis", tags=["video_analysis"])

app.include_router(api_router)

if __name__ == "__main__":
    logger.info(f"Starting uvicorn server on {settings.host}:{settings.api_port}")
    uvicorn.run(settings.app_run_name, host=settings.host, port=settings.api_port, reload=True, log_level="info")
