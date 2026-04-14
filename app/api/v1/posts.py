from http.client import HTTPException
from fastapi import APIRouter, Depends
from schemas.posts import PostCreate
from services.post_services import get_all_posts, insert_post
from api.v1.auth import current_active_user
from models.user import User

router = APIRouter()

# 1. all posts [Done]
# 2. all posts with limits [Done]
# 3. individual posts 
# 4. groups posts
# 5. create a posts
# 6. delete a posts

# Demo purpose:
@router.get("/read_posts/{user_id}")
def read_posts(user_id: str, offset: int = 0, limit: int = 10, user: User = Depends(current_active_user)):
    try:
        return {"posts": get_all_posts(user_id, offset, limit)}
    except Exception as e:
        return HTTPException(status_code=404, detail=str(e))

# getting the post by id
@router.get("/post/{id}")
def get_post_by_id(id: str):
    pass
    # return fake_data.get(id, {"error": "Post not found"})

@router.post("/create_post/{user_id}")
def create_post(post: PostCreate):
    return insert_post(post.user_id, post.title, post.content)