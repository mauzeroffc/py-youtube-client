from bs4 import BeautifulSoup
import requests
import os

from pyfzf.pyfzf import FzfPrompt

i = 1
sample = "https://invidious.snopyta.org"

title = input("Введите запрос: ")
urls = ""

page = int(input("Введите количество страниц: "))

titles_urls = {}

while True:
    url = f"https://invidious.snopyta.org/search?q={title}&&page={str(i)}&date=none&type=video&duration=none&sort=relevance"
    request = requests.get(url)
    request.encoding = 'KOI8'

    soup = BeautifulSoup(request.text, "lxml")

    href = soup.find_all("div", class_="h-box")

    if i <= page:
        for hrefs in href:
            hrefs = hrefs.find("a")

            if hrefs is not None:
                sublink = hrefs.get("href")

                if "watch" in sublink:
                    urls = sample + sublink

                    hrefs.div.decompose()
                    text = hrefs.p.text

                    titles_urls[text] = urls
        i += 1
    else:
        break

fzf = FzfPrompt()

inpt = fzf.prompt(titles_urls)
os.system(f"mpv {titles_urls[inpt[0]]}")
