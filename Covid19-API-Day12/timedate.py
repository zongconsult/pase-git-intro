import datetime


def get_date(number_of_days=1):

    today = datetime.datetime.today()

    yesterday = today - datetime.timedelta(days=amount)
    return yesterday.strftime("%m-%d-%Y")
