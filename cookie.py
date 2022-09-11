from time import time
from dateutil.parser import parse
from http.cookies import SimpleCookie


def get_cookie(key: str, cookies):
    simple_cookie = SimpleCookie()
    simple_cookie.load("ankiweb=eyJrIjogIkFudFNVWWxDRHpUMW9jNFEiLCAiYyI6IDEsICJ0IjogMTY2MjQ3NDgxOX0.kJZQXxA-YrNGAMD0BdSmBX46yIzMgVhP3ZJK5Vs2zNk; Max-Age=2592000; Path=/; expires=Thu, 06-Oct-2022 14:33:39 GMT; secure; HttpOnly; SameSite=lax")

    expires = int(parse(simple_cookie[key].get(
        "expires")).timestamp() - time())

    if key in simple_cookie.keys():
        return {"ankiweb": simple_cookie[key].value, "expires": expires}

    return None
