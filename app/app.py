from fastapi import FastAPI, HTTPException
from app.schemas import PostRequest, PostResponse

app = FastAPI()

@app.get("/hello-world")
def hello_world():
    return {"message": "Hello, World!"}

text_posts = {
    1: {"title": "First Post", "content": "This is the first post."},
    2: {"title": "Morning Thoughts", "content": "Starting the day with a fresh cup of coffee."},
    3: {"title": "Weekend Plans", "content": "Planning a short trip with friends this weekend."},
    4: {"title": "Learning Python", "content": "Today I learned how dictionaries work in Python."},
    5: {"title": "Book Recommendation", "content": "I just finished reading a great mystery novel."},
    6: {"title": "Workout Update", "content": "Completed a 30-minute run and felt amazing afterward."},
    7: {"title": "Movie Night", "content": "Watching a classic film tonight with popcorn."},
    8: {"title": "Project Progress", "content": "Made good progress on my side project today."},
    9: {"title": "Food Review", "content": "Tried a new pasta recipe and it turned out delicious."},
    10: {"title": "Final Post", "content": "This is the last post in the mock list."}
}

@app.get("/posts")
def get_all_posts(limit: int = None) -> list[PostResponse]:
    if limit:
        posts = list(text_posts.values())[:limit]
    return posts

@app.get("/posts/{post_id}")
def get_post(post_id: int) -> PostResponse:
    if post_id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(post_id)


@app.post("/posts")
def create_post(post: PostRequest) -> PostResponse:
    new_id = max(text_posts.keys()) + 1
    text_posts[new_id] = post
    return PostResponse(**post.dict(), id=new_id)



@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    if post_id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    del text_posts[post_id]
    return {"message": "Post deleted successfully"}