from pathlib import Path
from typing import Optional

from pydantic import BaseModel, BaseSettings, Field


APP_ROOT = Path(__file__).parent.parent

class AppSettings(BaseModel):
    """FastAPI specific configuration."""
    title: str = "Goodbye, Hello World!"
    description: str = "Hello, Functional FastAPI Web App"
    version: str = "0.0.7"
    docs_url: str = "/docs"


class GlobalSettings(BaseSettings):
    """Global settings."""

    more_settings: AppSettings = AppSettings()
    
    APP_DIR: Path = APP_ROOT

    ENV_STATE: Optional[str] = Field(None, env="ENV_STATE")

    MONGO_SCHEME: Optional[str] = None
    MONGO_HOST: Optional[str] = None
    MONGO_USER: Optional[str] = None
    MONGO_PASSWORD: Optional[str] = None
    MONGO_DB: Optional[str] = None

    FAVORITE_SONG: Optional[str] = None

    class Config:
        env_file = APP_ROOT.parent / ".env"


class DevSettings(GlobalSettings):
    """Development specific settings."""
    
    class Config:
        env_prefix = "DEV_"


class ProdSettings(GlobalSettings):
    """Production specific settings."""
    
    class Config:
        env_prefix = "PRD_"


class FactorySettings:
    """Callable class that loads Dev or Prod settings."""
    
    def __init__(self, env_state: Optional[str] = None):
        self.env_state = env_state

    def __call__(self):
        if self.env_state == "dev":
            return DevSettings()
        elif self.env_state == "prd":
            return ProdSettings()
        else:
            raise ValueError(f"Invalid env_state: {self.env_state}")

settings = FactorySettings(GlobalSettings().ENV_STATE)()
