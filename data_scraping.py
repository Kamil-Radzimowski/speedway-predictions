import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

URL = "https://speedwayekstraliga.pl/terminarz-i-wyniki/pge-ekstraliga/?y=2021"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

data = []

canvas = soup.find("div", class_="canvas")
canvas_top = canvas.find("div", class_="canvas__top")
article = canvas_top.find("article", class_="page")
container = article.find("div", class_="container")
page_inner = container.find("div", class_="page__inner")
main_schedule = page_inner.find("div", class_="main-schedule")
print(main_schedule)
schedule_list = main_schedule.find("div", class_="schedule")
divs = schedule_list.find_all("div")
for div in divs:
    grid = div.find("div", clas__="schedule_grid")
    items = grid.find_all("div")
    for item in items:
        events_list = item.find("ul")
        for li in events_list:
            match = {}
            a = li.find("a")
            inner = a.find("div")
            event = inner.find_all("div")
            team1 = event[0]
            result = event[1].find_all("span")[0].find_all("span")
            match["TEAM_1"] = team1.find("span").text
            match["TEAM_1_SCORE"] = result[0].text
            match["TEAM_2_SCORE"] = result[1].text
            match["TEAM_2"] = event[2].find("span").text
            data.append(match)


print(data)
# races = article.find_all("ul", class_="schedule-events")

# for race in races:
# print(race, end="\n"*2)
