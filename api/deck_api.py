from fastapi import Response, Request, APIRouter
import services.auth_service as auth_service
from helpers.cookie import get_cookie
import services.deck_service as deck_service

router = APIRouter()


@router.get("/decks")
def decks(request: Request):
    headers = {"Cookie": request.headers.get("cookie")}
    return deck_service.get_list(headers)


@router.get("/decks/{id}")
def decks(id: str, response: Response, request: Request):
    cookie_value = get_cookie("ankiweb_user", request.headers.get("cookie"))

    if cookie_value == None:
        headers = {"Cookie": request.headers.get("cookie")}
        user_cookie = auth_service.login_user(headers)
        cookie_value = user_cookie["ankiweb"]
        response.set_cookie(key="ankiweb_user", value=cookie_value)

    headers = {"Cookie": f"ankiweb={cookie_value}"}
    return deck_service.get(id, headers)
