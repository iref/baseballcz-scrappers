import scrapper


def print_scores(matches):
    for match in matches:
        print(f"* {match.team1} - {match.team2} {match.points1} {match.points2}")


def main():
    print("****** Baseball.cz Scores *****")

    site = scrapper.pull_site()
    matches = scrapper.scrape(site)
    print_scores(matches)


if __name__ == "__main__":
    main()
