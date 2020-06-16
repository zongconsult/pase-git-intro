from flask import Flask, jsonify, render_template
import csv
import datetime

from libs.cases import get_covid_cases

app = Flask(__name__)

today = datetime.datetime.today()
yesterday = today - datetime.timedelta(days=1)
day = yesterday.strftime("%m-%d-%Y")


URL = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{day}.csv"


@app.route("/api/v1", methods=["GET"])
def api():
    cases = get_covid_cases(URL)
    return jsonify({"total_cases": cases})


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
