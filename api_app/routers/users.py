from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/all")
async def get_all_users():
    return {"message": "Get all users"}


@router.get("/{user_id}")
async def get_user(user_id: str):
    return {"message": f"Get user with id {user_id}"}


@router.get("/{user_id}/favorites")
async def get_user_favorites(user_id: str):
    return {"message": f"Get user with id {user_id}"}


@router.post("/{user_id}/favorites")
async def add_user_favorite(user_id: str):
    return {"message": f"Add user with id {user_id}"}


@router.put("/{user_id}")
async def update_user(user_id: str):
    return {"message": f"Update user with id {user_id}"}


@router.delete("/{user_id}")
async def delete_user(user_id: str):
    return {"message": f"Delete user with id {user_id}"}


@router.delete("/{user_id}/favorites/{item_id}")
async def delete_user_favorite(user_id: str, item_id: str):
    return {"message": f"Delete user with id {user_id}"}
