from http.cookies import SimpleCookie


def get_cookie(key: str, cookies):
    simple_cookie = SimpleCookie()
    simple_cookie.load(cookies)
    return simple_cookie[key].value if key in simple_cookie.keys() else None
