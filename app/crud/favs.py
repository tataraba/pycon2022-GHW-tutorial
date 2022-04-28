from typing import Optional

from app.models.favs import FavoriteSongCreate, FavoriteSongDB


async def get_fav_song(song: str) -> dict:
    """Get a favorite song by song title"""
    fav_songs = await FavoriteSongDB.find_one(
        FavoriteSongDB.song_title == song
    )
    if not fav_songs:
        return {"message": f"{song} not found"}
    return fav_songs.dict()



async def create_fav_song(
    song_title: str, 
    artist: str, 
    description: Optional[str] = None
) -> FavoriteSongDB:
    """Create a favorite song"""
    fav_song = FavoriteSongCreate(
        song_title=song_title,
        artist=artist,
        description=description
    )

    await FavoriteSongDB(**fav_song.dict()).save()

    return fav_song