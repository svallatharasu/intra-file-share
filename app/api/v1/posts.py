from http.client import HTTPException
from fastapi import APIRouter, Depends, UploadFile, File, Form
from schemas.posts import PostResponse
from api.v1.auth import current_active_user
from models.user import User
from typing import Optional

router = APIRouter(tags=["posts"])

@router.get("/", response_model=list[PostResponse])
def read_all_posts(offset: int = 0, limit: int = 10, user: User = Depends(current_active_user)):
    pass

@router.get("/group/{group_id}", response_model=list[PostResponse])
def read_group_posts(group_id: int, offset: int = 0, limit: int = 10, user: User = Depends(current_active_user)):
    pass

@router.get("/{id}", response_model=PostResponse)
def get_post_by_id(id: int, user: User = Depends(current_active_user)):
    pass

@router.post("/", response_model=PostResponse)
def upload_post_file(
    group_id: Optional[int] = Form(None),
    file: UploadFile = File(...),
    user: User = Depends(current_active_user)
):
    pass