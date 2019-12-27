from loguru import logger

logger.add(
    "spider.log",
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss} - {level} - {file} - {line} - {message}",
    rotation="10 MB",
)
