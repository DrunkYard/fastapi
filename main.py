from fastapi import FastAPI # , Body
from pydantic import EmailStr, BaseModel
import uvicorn
app = FastAPI()

# чтобы принимать JSON Объекты
class CreateUser(BaseModel):
    email: EmailStr

@app.get("/")
def hello_index():
    return {
        "message": "Hello index!"
    }

# http://127.0.0.1:8000/hello?name=foobar
# принимаем из запроса переменную name
# если переменная пустая, то передастся "World!"
@app.get("/hello")
def hello(name: str = "World!"):
    name = name.strip().title()
    return {"message": f"Hello, {name}"}

# 
@app.post("/users/")
#  = Body() - чтобы данные передавались не в заголовке,
# http://127.0.0.1:8000/users/?email=test%40mail.com
# а в теле http://127.0.0.1:8000/users/
# def create_user(email: EmailStr = Body()):
    # return {
    #     "message": "success",
    #     "email": email,
    # }

@app.post("/calc/add")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b
    }

# чтобы принимать JSON Объекты
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email,
    }

@app.get("/items")
def list_items():
     return [
        "Item 1",
        "Item 2",
        "Item 3",
    ]

@app.get("/items/latest/")
def get_latest_item():
    return {"item": {"id": "0", "name" : "latest"}}

@app.get("/items/{item_id}/")
# item_id: int - должен быть только int
def get_item_by_id(item_id: int):
    return {
        "item": {
            "id": item_id,
        }
    }

if __name__ == '__main__':
    # для запуска приложения
    # reload=True - перезапуск при измененях в коде
    uvicorn.run('main:app', reload=True)