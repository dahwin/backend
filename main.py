from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
from database import *
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['https://www.queendahyun.com/']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Your routes go here

@app.get('/')
def read_root():
    return {'dahyun':'darwin'}
@app.get('/api/todo')
async def get_todo():
    return_dahwin = await fetch_all_todos()
    return return_dahwin

@app.get('/api/todo{title}',response_model=Todo)
async def get_todo_by_id(title):
    dahwin_res = await fetch_one_todo(title)
    if dahwin_res:
        return dahwin_res
    raise HTTPException(404,f'{title} is not found')


@app.post('/api/todo',response_model=Todo)
async def post_todo(todo:Todo):
    dahwin_res = await create_todo(todo.dict())
    if dahwin_res:
        return dahwin_res
    raise HTTPException('404 something went wrong')

@app.put('/api/todo{title}',response_model=Todo)
async def put_todo(title,desc):
    dahwin_res = await update_todo(title,desc)
    if dahwin_res:
        return dahwin_res
    raise HTTPException(404,f'{title} is not found')
@app.delete("/api/todo/{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the title {title}")
