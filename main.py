from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

####################
### Model Schema ###
####################
# title: string    # 
# content: string  # 
# published: bool  #
####################

class Model(BaseModel):
    title: str 
    content: str
    posted: bool = True
    likes: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Hello, World"}

@app.get("/posts/{id}")
async def get_post(id: int):
    return {"data": "test"}

@app.post("/posts")
async def make_post(message: Model):
    print(message.model_dump())
    return {"new_post": f"title: {message.title} | content: {message.content} | posted: {message.posted} | likes: {message.likes}"}

@app.put("/posts/{id}")
async def update_post(message: Model):
    return {}

@app.delete("/posts/{id}")
async def delete_post(id: int):
    return {}
