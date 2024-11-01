import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv('DATABASE_URL')
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY')

settings = Settings()
