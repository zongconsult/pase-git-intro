from .reader import get_csv_reader
from .countries import countries

covid_cases = []


def get_covid_cases(url):
    # csv_url = url + date + ".csv"
    reader = get_csv_reader(url)

    for row in reader:

        if row[3] in countries:
            covid_cases.append(
                {
                    "Country": row[3],
                    "Confirmed": row[7],
                    "Recoveries": row[9],
                    "Deaths": row[8],
                    "Active": row[10],
                }
            )

            return covid_cases
