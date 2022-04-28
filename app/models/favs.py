from typing import Optional

from beanie import Document
from pydantic import BaseModel, Field


class FavoriteSong(BaseModel):
    
    song_title: str
    artist: str
    description: Optional[str] = None


class FavoriteSongCreate(FavoriteSong):
    pass


class FavoriteSongDB(FavoriteSong, Document):
    pass

    class Collection:
        name = "favorite_songs"

