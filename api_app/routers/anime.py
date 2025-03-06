from fastapi import APIRouter

router = APIRouter(prefix="/anime", tags=["Anime"])


@router.get("/")
async def get_anime():
    pass


@router.get("/{anime_id}")
async def get_anime_by_id(anime_id: int):
    pass
