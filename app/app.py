from fastapi import FastAPI

app = FastAPI()

# simple list to store todos
todos = [
    {
        "id": "1",
        "Activity": "Working a project for 4 hours from 12:00PM"
    },
    {
        "id": "2",
        "Activity": "Training Model for Sentiment Project at 2:00PM"
    },

]

# base route
@app.get("/",tags=['ROOT'])
async def root() -> dict:
    return {
        "Ping": "Pong"
    }

# route for getting items inside todo
@app.get('/todo', tags=['todos'])
async def get_todo() -> dict:
    return {"data": todos}



