import requests
from bs4 import BeautifulSoup

URL = "https://speedwayekstraliga.pl/terminarz-i-wyniki/pge-ekstraliga/?y=2021"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

article = soup.find("article", class_="page")
container = article.find("div", class_="container")
page_inner = container.find("div", class_="page__inner")
main_schedule = page_inner.find("div", class_="main-schedule")
schedule_list = main_schedule.find_all("div")

# races = article.find_all("ul", class_="schedule-events")

# for race in races:
# print(race, end="\n"*2)
