import requests,csv
from io import StringIO


URL = 'https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
res = requests.get(URL)
data = res.content.decode('ascii','ignore')
csv_data = StringIO(data)
reader = csv.reader(csv_data)


for row in reader:
    print(row)

# print(data)