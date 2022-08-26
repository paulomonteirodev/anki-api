from typing import Union
from fastapi import FastAPI, Response, Request
import auth
from cookie import get_cookie
import deck
from models.login import Login


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World Teste"}


@app.post("/login")
def login(login: Login, response: Response):
    cookie = auth.login(login)
    response.set_cookie(key="ankiweb", value=cookie)
    return


@app.get("/decks")
def decks(request: Request):
    headers = {"Cookie": request.headers.get("cookie")}
    return deck.get_list(headers)


@app.get("/decks/{id}")
def decks(id: str, response: Response, request: Request):
    cookie_value = get_cookie("ankiweb_user", request.headers.get("cookie"))

    if cookie_value == None:
        headers = {"Cookie": request.headers.get("cookie")}
        user_cookie = auth.login_user(headers)
        response.set_cookie(key="ankiweb_user", value=user_cookie)
        cookie_value = user_cookie

    headers = {"Cookie": f"ankiweb={cookie_value}"}
    return deck.get(id, headers)
