from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.balldontlie.io/v1"
API_KEY = "f5fd1f14-e3bc-4abb-bbd1-5ce51857f635"

printer = PrettyPrinter()

headers = {
    "Authorization": API_KEY
}


def get_scoreboard():
    url = BASE_URL + "/games"

    response = get(url, headers=headers)
    games = response.json()["data"]

    for game in games:
        home_team = game["home_team"]
        away_team = game["visitor_team"]

        print("------------------------------------------")
        print(f"{home_team['abbreviation']} vs {away_team['abbreviation']}")
        print(f"{home_team['name']}: {game['home_team_score']}")
        print(f"{away_team['name']}: {game['visitor_team_score']}")
        print(f"Status: {game['status']}")


def get_stats():
    url = BASE_URL + "/stats"

    response = get(url, headers=headers)
    stats = response.json()["data"]

    for stat in stats:
        player = stat["player"]

        print("------------------------------------------")
        print(f"{player['first_name']} {player['last_name']}")
        print(f"Points: {stat['pts']}")
        print(f"Rebounds: {stat['reb']}")
        print(f"Assists: {stat['ast']}")


get_scoreboard()
