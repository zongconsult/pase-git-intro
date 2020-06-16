from .reader import get_csv_reader
from .countries import countries

covid_cases = []


def get_covid_cases(url):
    reader = get_csv_reader(url)

    for row in reader:
        if row[3] in countries:
            covid_cases.append(
                {
                    "Country": row[3],
                    "Confirmed": row[7],
                    "Deaths": row[8],
                    "Recovered": row[9],
                    "Active": row[10],
                }
            )
    return covid_cases
