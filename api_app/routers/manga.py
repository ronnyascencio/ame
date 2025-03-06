from fastapi import APIRouter

router = APIRouter(prefix="/manga", tags=["Manga"])


@router.get("/")
async def get_manga():
    pass


@router.get("/{manga_id}")
async def get_manga_by_id(manga_id: int):
    pass
