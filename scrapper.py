import bs4
import requests

from collections import namedtuple


Match = namedtuple('Match', 'team1, team2, points1, points2')
URL = "https://www.baseball.cz/"


def pull_site():
    resp = requests.get(URL)
    resp.raise_for_status()
    return resp


def scrape(site):
    soup = bs4.BeautifulSoup(site.text, "html.parser")
    scoreboard = soup.select_one("div#tab_rozpis div.rozpis")

    items = scoreboard.select('ul li ul li')
    matches = [scrape_match(item) for item in items]

    return matches


def scrape_match(match):
    teams = [t.getText() for t in match.select('.team')]
    points1 = match.select_one('.point1').getText().strip()
    points2 = match.select_one('.point2').getText().strip()

    if points1 and points2:
        points1 = int(points1)
        points2 = int(points2)
    else:
        points1 = 0
        points2 = 0

    return Match(
        team1=teams[0],
        team2=teams[1],
        points1=points1,
        points2=points2
    )



