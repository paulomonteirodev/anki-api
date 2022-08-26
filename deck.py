import json
import requests
from bs4 import BeautifulSoup
from config import base_url, base_user_url


def get_list(headers):
    url = f"{base_url}/decks/"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    buttons = soup.find_all("button")
    buttons = filter(lambda button: "data-full" in button.attrs, buttons)

    decks = list()
    for button in buttons:
        decks.append({"id": button["id"], "name": button["data-full"]})

    return decks


def get(id: str, headers):
    url = f"{base_url}/decks/select/{id}"
    headers["x-requested-with"] = "XMLHttpRequest"
    response = requests.post(url, headers=headers)

    url = f"{base_user_url}/study/getCards"
    payload = '{"answers":[],"saveAnswersOnly":false}'
    headers["Content-Type"] = "text/plain"
    response = requests.post(url, data=payload, headers=headers, verify=False)

    return json.loads(response.text)
