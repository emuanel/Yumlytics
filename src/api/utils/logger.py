import logging
import os

from config import settings

def get_logger(name: str) -> logging.Logger:
    logging.basicConfig(
        level=settings.logging.parsed_log_level, format="%(asctime)s | %(name)s | %(levelname)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    logger = logging.getLogger(name)

    file_handler = logging.FileHandler(os.path.join(settings.logging.log_dir, f"{name}.log"))
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S"))

    logger.addHandler(file_handler)

    return logger

logger_video_analysis = get_logger("video_analysis")
