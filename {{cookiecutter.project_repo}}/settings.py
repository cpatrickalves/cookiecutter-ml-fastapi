from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret
from typing import List
from core.logging import InterceptHandler
from loguru import logger
import logging
import sys

# Config will be read from environment variables and/or ".env" files.
config = Config(".env")

API_PREFIX = "/api"
VERSION = "{{cookiecutter.version}}"
DEBUG = config("DEBUG", cast=bool, default=False)
MAX_CONNECTIONS_COUNT = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
MIN_CONNECTIONS_COUNT = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)
SECRET_KEY = config("SECRET_KEY", cast=Secret, default="")

PROJECT_NAME = config("PROJECT_NAME", default="{{cookiecutter.project_name}}")

# logging configuration
LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
logging.basicConfig(
    handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL
)
logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])

MODEL_PATH = config("MODEL_PATH", default="{{cookiecutter.machine_learn_model_path}}")
MODEL_NAME = config("MODEL_NAME", default="{{cookiecutter.machine_learn_model_name}}")
