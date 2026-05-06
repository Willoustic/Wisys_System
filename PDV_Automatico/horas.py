from datetime import datetime
from time import sleep

def hora():
    h = datetime.now().hour
    m = datetime.now().minute
    s = datetime.now().second

    hour = f'{h}:{m}:{s}'

    return hour
