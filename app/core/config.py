import os
from functools import lru_cache

from dotenv import load_dotenv


class Settings:
    def __init__(self):
        self.DATETIME_TIMEZONE = os.getenv("DATETIME_TIMEZONE")
        self.DATETIME_FORMAT = os.getenv("DATETIME_FORMAT")
        self.MYSQL_USER = os.getenv("MYSQL_USER")
        self.MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
        self.MYSQL_HOST = os.getenv("MYSQL_HOST")
        self.MYSQL_PORT = os.getenv("MYSQL_PORT")
        self.MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
        self.MYSQL_CHARSET = os.getenv("MYSQL_CHARSET")


@lru_cache
def get_settings() -> Settings:
    """
    A service instance under single-process multithreading still has only one instance
    Get global configuration
    """
    load_dotenv()
    return Settings()


settings = get_settings()
