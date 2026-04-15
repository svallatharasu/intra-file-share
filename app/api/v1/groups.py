from fastapi import APIRouter, Depends
from api.v1.auth import current_active_user
from schemas.groups import GroupCreate, GroupResponse
from models.user import User

router = APIRouter(tags=["groups"])

@router.post("/", response_model=GroupResponse)
def create_group(group: GroupCreate, user: User = Depends(current_active_user)):
    pass

@router.post("/{group_id}/members")
def add_member(group_id: int, target_user_id: int, user: User = Depends(current_active_user)):
    pass

@router.get("/search")
def search_groups(query: str, user: User = Depends(current_active_user)):
    pass
