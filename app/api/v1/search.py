from fastapi import APIRouter, Depends
from api.v1.auth import current_active_user
from models.user import User

router = APIRouter(tags=["search"])

@router.get("/")
def semantic_search_files(query: str, user: User = Depends(current_active_user)):
    pass
