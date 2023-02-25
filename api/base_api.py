from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_cookies(request: Request):
    cookies = request.headers.get("cookie")
    if request.headers.get("cookie") == None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    return cookies
