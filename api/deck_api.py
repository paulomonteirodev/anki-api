from fastapi import Depends, Response, Request, APIRouter
import services.auth_service as auth_service
import helpers.cookie as cookie
import services.deck_service as deck_service
from .base_api import get_cookies

router = APIRouter()


@router.get("/decks")
async def decks(cookies=Depends(get_cookies)):
    headers = {"Cookie": cookies}
    return deck_service.get_list(headers)


@router.get("/decks/{id}")
async def decks(id: str, response: Response, cookies=Depends(get_cookies)):
    cookie_value = cookie.get_value("ankiweb_user", cookies)

    if cookie_value == None:
        headers = {"Cookie": cookies}
        user_cookie = auth_service.login_user(headers)
        cookie_value = user_cookie["ankiweb"]
        response.set_cookie(key="ankiweb_user", value=cookie_value)

    headers = {"Cookie": f"ankiweb={cookie_value}"}
    return deck_service.get(id, headers)
