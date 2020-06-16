import requests, csv
from io import StringIO
from app import URL

res = requests.get(URL)

# display the data as text
# print(res.txt)

# display the data as bytes
# print(res.content)

# convert the content of the data to a string and print
# data =res.content.decode("ascii", "ignore")
# print (data)

data = res.content.decode("ascii", "ignore")
csv_data = StringIO(data)

reader = csv.reader(csv_data)


for row in reader:
    print(row)
