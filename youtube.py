from bs4 import BeautifulSoup
import requests
import os
import time

from pyfzf.pyfzf import FzfPrompt

sample = "https://invidious.snopyta.org"

various = ["Канал", "Запрос", "Плейлист"]
date_filtres = ["none", "today", "hour", "week", "month", "year"]
duration_filres = ["none", "short", "long", "medium"]
sort_filtres = ["relevance(актуальность)", "raiting(рейтинг)", "date(дата загрузки)", "views(просмотры)"]

fzf = FzfPrompt()

names_urls = {}
names_videos_channel = {}
names_video_playlist = {}
titles_urls = {}
names_playlist = {}

print("Сейчас надо будет выбрать вашу операционную систему: ")
time.sleep(3)

name_os = fzf.prompt(["Windows", "Linux"])

inpt_various = fzf.prompt(various)

def channel_video_parser(url2, num_page):
    b = 1

    while True:
        req = requests.get(url2)
        if name_os[0] == "Windows":
            req.encoding = "1250"
        elif name_os[0] == "Linux":
            req.encoding = "KOI8"

        sp = BeautifulSoup(req.text, "lxml")

        hrf = sp.find_all("div", class_="pure-u-1 pure-u-md-1-4")
        duration = sp.find_all("div", class_="thumbnail")

        if b <= num_page:
            for hrfs1 in hrf:
                hrfs1 = hrfs1.find("a")

                if hrfs1 is not None:
                    sublink2 = hrfs1.get("href")

                    if "/watch?" in sublink2:
                        urls2 = sample + sublink2

                        hrfs1.div.decompose()
                        txt1 = hrfs1.p.text

                        names_videos_channel[txt1] = urls2
            b += 1
        else:
            break

    inpt1 = fzf.prompt(names_videos_channel)
    os.system(f"mpv {names_videos_channel[inpt1[0]]}")

def playlist_video_parser(url4, num_page1):
    d = 1

    while True:
        req2 = requests.get(url4)
        if name_os[0] == "Windows":
            req2.encoding = "1250"
        elif name_os[0] == "Linux":
            req2.encoding = "KOI8"

        sp3 = BeautifulSoup(req2.text, "lxml")

        hrf2 = sp3.find_all("div", class_="pure-u-1 pure-u-md-1-4")

        if d <= num_page1:
            for hrfs3 in hrf2:
                hrfs3 = hrfs3.find("a")

                if hrfs3 is not None:
                    sublink3 = hrfs3.get("href")

                    if "/watch?" in sublink3:
                        urls4 = sample + sublink3

                        hrfs3.div.decompose()
                        txt3 = hrfs3.p.text

                        names_videos_playlist[txt3] = urls4
            d += 1
        else:
            break

    inpt4 = fzf.prompt(names_videos_playlist)
    os.system(f"mpv {names_videos_playlist[inpt4[0]]}")

def playlists():
    c = 1

    filter = input("Нужно ли добавить фильтр (сортировка по времени и т.д (д/н))? ")

    if (filter == "д"):
        print("Выберите фильтр даты: ")
        time.sleep(3)
        date = fzf.prompt(date_filtres)

        print("Выберите фильр длительности: ")
        time.sleep(3)
        duration = fzf.prompt(duration_filres)

        print("Выберите фильтр сортировки: ")
        time.sleep(3)
        sort = fzf.prompt(sort_filtres)
        if sort[0] == "":
            sort[0] = "relevance"

        url_playlist = f"https://invidious.snopyta.org/search?q={name_of_playlist}&&page={c}&date={date[0]}&type=playlist&duration={duration[0]}&sort={sort[0]}"

    else:
        url_playlist = f"https://invidious.snopyta.org/search?q={name_of_playlist}&&page={c}&date=none&type=playlist&duration=none&sort=relevance"

    while True:
        req1 = requests.get(url_playlist)
        if name_os[0] == "Windows":
            req1.encoding = "1250"
        elif name_os[0] == "Linux":
            req1.encoding = "KOI8"

        sp1 = BeautifulSoup(req1.text, "lxml")

        hrf1 = sp1.find_all("div", class_="pure-u-1 pure-u-md-1-4")

        if c <= page_playlist:
            for hrfs1 in hrf1:
                hrfs1 = hrfs1.find("a")

                if hrfs1 is not None:
                    sbl1 = hrfs1.get("href")

                    if "/playlist?" in sbl1:
                        urls3 = sample + sbl1

                        hrfs1.div.decompose()
                        txt1 = hrfs1.p.text

                        names_playlist[txt1] = urls3
            c += 1
        else:
            break

    inpt2 = fzf.prompt(names_playlist)

    page3 = input("Введите количество страниц для плейлиста (по умолчанию 1): ")

    if (page3 == ""):
        page3 = 1
    else:
        page3 = int(page3)

    url5 = names_playlist[inpt2[0]]

    channel_video_parser(url5, page3)

def channels():
    a = 1

    filter = input("Нужно ли добавить фильтр (сортировка по времени и т.д (д/н))? ")

    if (filter == "д"):
        print("Выберите фильтр даты: ")
        time.sleep(3)
        date = fzf.prompt(date_filtres)

        print("Выберите фильр длительности: ")
        time.sleep(3)
        duration = fzf.prompt(duration_filres)

        print("Выберите фильтр сортировки: ")
        time.sleep(3)
        sort = fzf.prompt(sort_filtres)
        if sort[0] == "":
            sort[0] = "relevance"

        url_channel = f"https://invidious.snopyta.org/search?q={name_of_channel}&&page={a}&date={date[0]}&type=channel&duration={duration[0]}&sort={sort[0]}"

    else:
        url_channel = f"https://invidious.snopyta.org/search?q={name_of_channel}&&page={a}&date=none&type=channel&duration=none&sort=relevance"

    while True:
        request1 = requests.get(url_channel)
        if name_os[0] == "Windows":
            request1.encoding = "1250"
        elif name_os[0] == "Linux":
            request1.encoding = "KOI8"

        soup1 = BeautifulSoup(request1.text, "lxml")

        href1 = soup1.find_all("div", class_="pure-u-1 pure-u-md-1-4")

        if a <= page_channel:
            for hrefs1 in href1:
                hrefs1 = hrefs1.find("a")

                if hrefs1 is not None:
                    sublink1 = hrefs1.get("href")

                    if "/channel/" in sublink1:
                        urls1 = sample + sublink1

                        hrefs1.center.decompose()
                        text1 = hrefs1.p.text

                        names_urls[text1] = urls1
            a += 1
        else:
            break

    inpt = fzf.prompt(names_urls)
    page1 = input("Введите количество страниц для канала (по умолчанию 1): ")

    if (page1 == ""):
        page1 = 1
    else:
        page1 = int(page1)

    url3 = names_urls[inpt[0]]

    channel_video_parser(url3, page1)
    #channel_video_page = int(input("Введи количество страниц: "))

def videos():
    i = 1

    filter = input("Нужно ли добавить фильтр (сортировка по времени и т.д (д/н))? ")

    if (filter == "д"):
        print("Выберите фильтр даты: ")
        time.sleep(3)
        date = fzf.prompt(date_filtres)

        print("Выберите фильр длительности: ")
        time.sleep(3)
        duration = fzf.prompt(duration_filres)

        print("Выберите фильтр сортировки: ")
        time.sleep(3)
        sort = fzf.prompt(sort_filtres)
        if sort[0] == "":
            sort[0] = "relevance"

        url = f"https://invidious.snopyta.org/search?q={title}&&page={str(i)}&date={date[0]}&type=video&duration={duration[0]}&sort={sort[0]}"

    else:
        url = f"https://invidious.snopyta.org/search?q={title}&&page={str(i)}&date=none&type=video&duration=none&sort=relevance"

    while True:
        request = requests.get(url)
        if name_os[0] == "Windows":
            request.encoding = "1250"
        elif name_os[0] == "Linux":
            request.encoding = "KOI8"

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

    inpt = fzf.prompt(titles_urls)
    os.system(f"mpv {titles_urls[inpt[0]]}")

if inpt_various[0] == "Канал":
    name_of_channel = input("Введите название канала: ")
    page_channel = input("Введите количество страниц (по умолчанию 1): ")

    if (page_channel == ""):
        page_channel = 1
    else:
        page_channel = int(page_channel)

    name_urls = ""

    channels()
elif inpt_various[0] == "Запрос":
    title = input("Введите запрос: ")
    urls = ""

    page = input("Введите количество страниц (по умолчанию 1): ")

    if (page == ""):
        page = 1
    else:
        page = int(page)

    videos()
elif inpt_various[0] == "Плейлист":
    name_of_playlist = input("Введите название плейлиста: ")
    page_playlist = input("Введите количество страниц (по умолчанию 1): ")

    if (page_playlist == ""):
        page_playlist = 1
    else:
        page_playlist = int(page_playlist)

    name_playlist = ""

    playlists()
