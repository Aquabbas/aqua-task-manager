import os
from fastapi import FastAPI, HTTPException
from model import Todo
# from decouple import config
from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo,
)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Possible Soltuion For Render Deployed (React) App to Connect w/ Render Deployed (FastAPI) App
# import os
# origins =  REACT_URL,https://yourfrontendapp2.com
# REACT_URL = config('REACT_URL')
REACT_URL = os.environ.get('REACT_URL')
origins = [
    REACT_URL,
]

# Middleware is software that acts as a bridge between an operating system or database and applications, especially on a network.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # Possible Solution For Render Deployed React App
    #allow_origins=os.environ.get("uri").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/api/todo")
async def get_todo():
    print("Received GET request at /api/todo")  # Add this line for debugging
    response = await fetch_all_todos()
    return response

@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_title(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")

@app.post("/api/todo/", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.put("/api/todo/{title}/", response_model=Todo)
async def put_todo(title: str, desc: str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")

@app.delete("/api/todo/{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the title {title}")