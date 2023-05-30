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


# route for adding data to list
@app.post("/todo", tags=['todos'])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {
        "data": "A todo has been added"
    }

#updating the todos
@app.put("/todo/{id}", tags=['todos'])
async def update_todo(id:int, body:dict) -> dict:
    for todo in todos:
        if int(todo['id']) == id:
            todo['Activity'] = body['Activity']
            return {
                "data": f'Todo with  id {id} has been updated'
            }
    return {
        "data": f"Todo with id {id} was not found"
    }

# delete item from list
@app.delete("/todo/{id}", tags=['todos'])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo['id']) == id:
            todos.remove(todo)
            return {
                "data": f'Todo with  id {id} has been deleted'
            }
    return {
        "data": f"Todo with id {id} was not found"
    }
