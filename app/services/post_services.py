fake_data = {
    "user1": [
        {"title": "Post 1", "content": "Content of Post 1"},
        {"title": "Post 2", "content": "Content of Post 2"},
        {"title": "Post 3", "content": "Content of Post 3"},
    ],
    "user2": [
        {"title": "Another Post", "content": "Hello world"}
    ]
}

def get_all_posts(user_id: str, offset: int, limit: int):
    posts = fake_data.get(user_id, [])
    return posts[offset:offset + limit]

def insert_post(user_id: str, title: str, content: str):
    new_post = {"title": title, "content": content}
    if user_id in fake_data:
        fake_data[user_id].append(new_post)
    else:
        fake_data[user_id] = [new_post]
    return new_post