import os
from typing import List

from loguru import logger
from pydantic import BaseSettings


class Config(BaseSettings):
    enable_docs: bool = True
    profile_endpoints: bool = True
    cors_origins: List[str] = ["*"]


stage = os.environ.get("STAGE")

if not stage:
    config = Config()
else:
    config = Config(_env_file=f".env.{stage.lower()}", _env_file_encoding="utf-8")  # type: ignore[call-arg]

logger.info(f"Config: {config}")
