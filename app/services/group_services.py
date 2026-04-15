from sqlalchemy.orm import Session
from models.group import Group
from models.user import User, GroupMembership
from schemas.groups import GroupCreate

def create_group(db: Session, group_in: GroupCreate, user_id: int):
    pass

def search_groups(db: Session, query: str):
    pass

def add_user_to_group(db: Session, group_id: int, user_id: int):
    pass
