import requests, csv
from io import StringIO

csv_url = "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/06-15-2020.csv"


def get_csv_reader(csv_url):
    res = requests.get(csv_url)
    data = res.content.decode("ascii", "ignore")
    return csv.reader(StringIO(data))
