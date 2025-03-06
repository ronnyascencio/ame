from fastapi import APIRouter

router = APIRouter(prefix="/reviews", tags=["Reviews"])


@router.get("/{item_id}")
async def get_review(item_id: str):
    return {"message": f"Get review with id {review_id}"}


@router.post("/")
async def create_review():
    return {"message": f"Create review"}


@router.delete("/{review_id}")
async def delete_review(review_id: str):
    return {"message": f"Delete review with id {review_id}"}
