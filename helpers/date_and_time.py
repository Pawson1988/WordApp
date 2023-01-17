from datetime import datetime


def get_date():
    today = datetime.today()
    return today.strftime("%H-%M-%S %d-%m-%y")

