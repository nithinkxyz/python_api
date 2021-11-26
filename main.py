from typing import Optional
from fastapi import FastAPI
from fastapi.param_functions import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()


# data validation: title - string, content - string
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "Mathematician", "content": "Newton", "id": 1}, {"title": "Physicist", "content":  "Einstein", "id": 2}]


def find_post(id):
    for i in my_posts:
        if i["id"] == id:
            return i

@app.get("/")
def root():
    return {"PYTHON"}

@app.get("/posts")
def get_posts():
    return my_posts

@app.post("/posts")
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int):
    return find_post(id)
    