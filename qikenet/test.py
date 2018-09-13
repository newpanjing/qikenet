import datetime


def utc_date(text):
    date = datetime.datetime.strptime(text, '%Y-%m-%dT%H:%M:%SZ')
    return date

# print(utc_date('2018-08-31T17:13:59Z'))

# import datetime


# print(date)