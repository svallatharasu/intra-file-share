from sqlalchemy.orm import Session
from models.comment import Comment
from schemas.comments import CommentCreate

def add_message_to_file(db: Session, post_id: int, user_id: int, comment_in: CommentCreate):
    pass

def get_file_messages(db: Session, post_id: int):
    pass
