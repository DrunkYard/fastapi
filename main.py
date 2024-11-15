from fastapi import FastAPI # , Body
# from pydantic import EmailStr, BaseModel
import uvicorn

from item_views import router as items_router 
from users.views import router as users_router

app = FastAPI()
# подключение маршрута
# prefix="/items-views/" - если нужно переопределить префикс
app.include_router(items_router) # prefix="/items-views/")
app.include_router(users_router)

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

# @app.post("/users/")
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

if __name__ == '__main__':
    # для запуска приложения
    # reload=True - перезапуск при измененях в коде
    uvicorn.run('main:app', reload=True)