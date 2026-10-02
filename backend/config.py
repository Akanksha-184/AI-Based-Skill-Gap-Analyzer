import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mongodb_uri: str = "mongodb://localhost:27017"
    database_name: str = "career_gap_analyzer"
    openai_api_key: str = ""
    spacy_model: str = "en_core_web_sm"

    class Config:
        env_file = ".env"

settings = Settings()
