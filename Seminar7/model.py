import datetime


def newYear():
    current_date = datetime.datetime.now()
    new_year = datetime.datetime(current_date.year + 1,1,1)
    # print(f'{(new_year-current_date).days} до нового года')
    return (new_year-current_date).days

