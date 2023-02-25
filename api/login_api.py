from fastapi import Response, APIRouter
import services.auth_service as auth_service
from models.login import Login

router = APIRouter()


@router.post("/login")
def login(login: Login, response: Response):
    cookie = auth_service.login(login)
    response.set_cookie(
        key="ankiweb", value=cookie["ankiweb"], expires=cookie["expires"])
    return "Login Realizado com sucesso"
