from pydoc import doc
from typing import Optional

from app.core.config import settings
from app.models.favs import FavoriteSongDB
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import AnyUrl, BaseSettings, validator


class DatabaseConnector(BaseSettings):
    """Load database settings and build valid URI"""

    MONGO_DB_URI: Optional[AnyUrl] = None

    @validator("MONGO_DB_URI", pre=True, check_fields=False)
    def uri_is_valid(cls, v):
        if isinstance(v, AnyUrl):
            return v

        if settings.MONGO_HOST in ("localhost", "127.0.0.1"):
            try:
                return AnyUrl.build(
                    scheme=settings.MONGO_SCHEME,
                    host = settings.MONGO_HOST,
                    port = settings.MONGO_PORT,
                    user = settings.MONGO_USER,
                    password = settings.MONGO_PASSWORD,
                    path=f"/{settings.MONGO_DB}",
                    query="rewtryWrites=true&w=majority",
                )
            except Exception:
                raise AttributeError(v)
        try:
            return AnyUrl.build(
                scheme=settings.MONGO_SCHEME,
                host = settings.MONGO_HOST,
                user = settings.MONGO_USER,
                password = settings.MONGO_PASSWORD,
                path=f"/{settings.MONGO_DB}",
                query="retryWrites=true&w=majority",
            )
        except Exception:
            raise AttributeError(v)

    async def initialize_db(self) -> None:
        """start db client with Beanie and load models"""

        client = AsyncIOMotorClient(self.MONGO_DB_URI)
        models = [FavoriteSongDB]

        try:
            await init_beanie(
                database=client[settings.MONGO_DB],
                document_models=models
            )
            print(f'Connected to {settings.MONGO_DB}')
        except Exception:
            raise ConnectionError


db = DatabaseConnector()