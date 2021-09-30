import requests
from bs4 import BeautifulSoup as bs


ENDPOINT = {
    "base": "https://orari-be.divsi.unimi.it",
    "home": "/EasyRoom/index.php?_lang=it",
    "rooms": "/EasyRoom/index.php?vista=month&content=view_prenotazioni&_lang=it&area={}&room=582",
}


def area_from_string(string: str):
    for x in string.split("&"):
        if "area" in x:
            return x.split("=")[1]


def get_area():
    resp = requests.get(ENDPOINT["base"] + ENDPOINT["home"])
    soup = bs(resp.text, "lxml")
    links = soup.find_all("a")
    ris = []
    for link in links:
        if link.img and "area=" in link["href"]:
            ris.append((area_from_string(link["href"]), link.find("img")["alt"]))
    return ris


def get_rooms(area):
    resp = requests.get(ENDPOINT["base"] + ENDPOINT["rooms"].format(area))
    soup = bs(resp.text, "lxml")
    select = soup.find_all("select", attrs={"name": "url"})[0]
    return [(option["value"], option.string) for option in select.find_all("option")]


def main():
    pass


if __name__ == "__main__":
    main()
