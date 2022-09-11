from fastapi import Response, Request
from app import create_app
import auth
from cookie import get_cookie
import deck
from models.login import Login
from fastapi.responses import RedirectResponse

app = create_app()


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse("/docs")


@app.post("/login")
def login(login: Login, response: Response):
    cookie = auth.login(login)
    response.set_cookie(
        key="ankiweb", value=cookie["ankiweb"], expires=cookie["expires"])
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
        cookie_value = user_cookie["ankiweb"]
        response.set_cookie(key="ankiweb_user", value=cookie_value)

    headers = {"Cookie": f"ankiweb={cookie_value}"}
    return deck.get(id, headers)
