import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class APPLICATION_SETTING(BaseSettings):
    # HOST_IP = os.getenv("HOST_IP")
    # HOST_PORT = int(os.getenv("HOST_PORT"))
    # DEBUG = os.getenv("DEBUG", False)

    HOST_IP : str
    HOST_PORT : int
    DEBUG : bool 

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

class DATABASE_SETTING(BaseSettings):
    POSTGRES_USERNAME: str
    POSTGRES_PORT: str
    POSTGRES_IP: str
    POSTGRES_PASSWORD : str
    POSTGRES_DATABASE: str 
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

database_settings = DATABASE_SETTING()


applicaion_setting = APPLICATION_SETTING()