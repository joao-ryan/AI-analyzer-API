import logging
import sys
import time
from pythonjsonlogger import jsonlogger
from fastapi import Request

def setup_logging():
    logger = logging.getLogger()
    logHandler = logging.StreamHandler(sys.stdout)
    formatter = jsonlogger.JsonFormatter(
        '%(timestamp)s %(severity)s %(name)s %(message)s %(request_id)s %(endpoint)s %(duration)s'
    )
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
    logger.setLevel(logging.INFO)
    return logger

logger = setup_logging()

async def logging_middleware(request: Request, call_next):
    start_time = time.time()
    request_id = request.headers.get("X-Request-ID", "unknown")

    response = await call_next(request)

    process_time = time.time() - start_time
    logger.info(
        "requisição processada",
        extra={
            "request_id": request_id,
            "endpoint": request.url.path,
            "duration": f"{process_time:.4f}s",
            "severity": "INFO"
        }
    )
    return response
