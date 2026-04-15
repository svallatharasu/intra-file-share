from sqlalchemy.orm import Session
from fastapi import UploadFile
from models.post import Post

def get_all_posts(db: Session, user_id: int, offset: int, limit: int):
    pass

def get_group_posts(db: Session, group_id: int, offset: int, limit: int):
    pass

def insert_post(db: Session, user_id: int, group_id: int | None, file: UploadFile):
    # TODO: Implement file saving logic (local disk or S3)
    pass