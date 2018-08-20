from flask import Flask, jsonify

import scrapper

app = Flask(__name__)


@app.route("/scores")
def scores():
    site = scrapper.pull_site()
    scores = scrapper.scrape(site)
    return jsonify({"scores": scores})


if __name__ == '__main__':
    app.run(debug=True)
