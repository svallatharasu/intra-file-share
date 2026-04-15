from sqlalchemy.orm import Session
from schemas.sidebar import SidebarItem
from datetime import datetime, UTC

def get_user_sidebar(db: Session, user_id: int) -> list[SidebarItem]:
    """
    Fetches a WhatsApp-style sidebar listing groups and direct message users,
    sorted by the latest activity (files uploaded or comments added).
    """
    # TODO: Write complex SQLAlchemy query:
    # 1. Fetch all groups the user is in. Find the latest Post/Comment timestamp in each group.
    # 2. Fetch all direct files (recipient_id=user_id OR owner_id=user_id and group_id is Null).
    #    Group these by the *other* user involved and find their latest Post/Comment timestamp.
    # 3. Combine both lists, map them to SidebarItem schemas.
    # 4. Sort descending by last_activity_time.
    
    # Placeholder return
    return []
