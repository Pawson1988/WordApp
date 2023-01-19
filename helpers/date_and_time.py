from datetime import datetime


def get_date():
    today = datetime.today()
    return today.strftime("%d-%m-%y")

def get_time():
    time = datetime.today()
    return time.strftime("%H:%M:%S")