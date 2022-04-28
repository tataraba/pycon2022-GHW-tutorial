from fastapi import APIRouter
from app.crud.favs import get_fav_song, create_fav_song
from app.models.favs import FavoriteSongDB, FavoriteSongCreate

router = APIRouter()


@router.get("/")
async def home_dir():
    """The home directory."""
    return {"message": "Ugh, Hello... World..."}


@router.get("/{song}")
async def retrieve_song(song: str):
    """Get a favorite song by song title"""
    return await get_fav_song(song)


@router.post("/add_song")
async def create_song(song_entry: FavoriteSongCreate):
    """Create a favorite song"""
    return await create_fav_song(**song_entry.dict())