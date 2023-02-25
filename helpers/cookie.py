from time import time
from dateutil.parser import parse
from http.cookies import SimpleCookie


def get(key: str, cookies):
    simple_cookie = SimpleCookie()
    simple_cookie.load(cookies)

    if key not in simple_cookie.keys():
        return None

    cookie = simple_cookie[key]
    expires_cookie = cookie.get("expires")

    expires = None
    if expires_cookie:
        expires = int(parse(expires_cookie).timestamp() - time())

    return {key: cookie.value, "expires": expires}


def get_value(key: str, cookies):
    cookie_object = get(key, cookies)

    return None if cookie_object == None else cookie_object[key]
