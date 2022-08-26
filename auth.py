import requests
from config import base_url

from cookie import get_cookie
from models.login import Login  # Python 2: import cookielib as cookiejar


def login(login: Login):
    url = f"{base_url}/account/login"
    payload = f"submitted=1&csrf_token=eyJvcCI6ICJsb2dpbiIsICJpYXQiOiAxNjYxNTIyNTEyLCAiaXAiOiAiMTg3LjEyNy4xNTEuNTkifQ.AXq1BibGCtLFVJfv-WFGkGRDy9u382s-XZ3Hrg1UspY&username={login.email}&password={login.password}"
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
