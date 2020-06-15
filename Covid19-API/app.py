from flask import Flask, jsonify

# Importing CSV to read URL
import csv

app = Flask(__name__)

URL = "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/06-15-2020.csv"


# @app.route("/", methods=["POST"])
# def index():
#     return jsonify({"Hello World": "Henry"})


@app.route("/api/v1", methods=["GET"])
def index():
    return jsonify({"total_cases": 5000})


# @app.route("/")
# def index():
#     return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)
