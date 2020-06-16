from flask import Flask, jsonify
import requests, csv
import datetime
from libs.cases import get_covid_cases


app = Flask(__name__)

# today =

# yesterday =

# day =

base_url = "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/06-15-2020.csv"

res = requests.get(base_url)


@app.route("/api/v1", methods=["GET"])
@app.route("/api/v1/<date>", methods=["GET"])
def index():
    # print(res)
    cases = get_covid_cases(base_url)
    return jsonify({"total_cases": cases})


# def index():

if __name__ == "__main__":
    app.run(debug=True)
