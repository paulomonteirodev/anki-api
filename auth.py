from bs4 import BeautifulSoup
import requests
from config import base_url

from cookie import get_cookie
from models.login import Login  # Python 2: import cookielib as cookiejar
import re


def get_csrf_token():
    url = f"{base_url}/account/login"
    response = requests.get(url, allow_redirects=False)
    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.select_one("input[name=csrf_token]")
    return result.attrs["value"]


def login(login: Login):
    url = f"{base_url}/account/login"
    payload = f"submitted=1&csrf_token={get_csrf_token()}&username={login.email}&password={login.password}"
    headers = {
        "cookie": "ankiweb=login",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    response = requests.post(url, headers=headers,
                             data=payload, allow_redirects=False)

    return get_cookie("ankiweb", response.headers["set-cookie"])


def login_user(headers):
    url = f"{base_url}/account/userAuth?rt=/study/"
    response = requests.get(url, headers=headers,
                            verify=False, allow_redirects=False)
    redirect_url = response.headers["location"]

    headers["cookie"] = "ankiweb=login"
    response = requests.get(
        redirect_url, headers=headers, verify=False, allow_redirects=False
    )

    return get_cookie("ankiweb", response.headers["set-cookie"])
