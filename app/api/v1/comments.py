from fastapi import APIRouter, Depends
from api.v1.auth import current_active_user
from models.user import User
from schemas.comments import CommentCreate, CommentResponse

router = APIRouter(tags=["comments"])

@router.post("/{post_id}", response_model=CommentResponse)
def add_comment(post_id: int, comment: CommentCreate, user: User = Depends(current_active_user)):
    pass

@router.get("/{post_id}", response_model=list[CommentResponse])
def get_comments(post_id: int, user: User = Depends(current_active_user)):
    pass
