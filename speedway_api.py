import requests


def getData(year):
    result = []
    url = f"https://stats.speedwayekstraliga.pl/api/v1/matches/schedule?rand=020520221302&s={year}&r=1"
    response = requests.get(url)
    data = response.json()["data"]
    for entry in data:
        match = {"season": entry["season"], "team_1": entry["card_teams"][0]["team_shortcut"],
                 "team_2": entry["card_teams"][1]["team_shortcut"],
                 "team_1_score": entry["card_teams"][0]["match_score"],
                 "team_2_score": entry["card_teams"][1]["match_score"]}
        result.append(match)

    print(result)
