from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class DatabaseSettings(BaseSettings):
    DB_USER:str
    DB_PASSWORD:str
    DB_NAME:str
    DB_HOST:str
    DB_PORT:int


def init_db_settings() -> DatabaseSettings:
    return DatabaseSettings()
